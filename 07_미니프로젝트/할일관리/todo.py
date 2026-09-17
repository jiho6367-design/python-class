"""JSON 파일에 내용을 저장하는 간단한 할 일 관리 프로그램입니다."""

import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks(file_path: Path = DATA_FILE) -> list[dict]:
    """JSON 파일에서 할 일 목록을 불러옵니다."""
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            raise ValueError

        for task in tasks:
            if not (
                isinstance(task, dict)
                and isinstance(task.get("id"), int)
                and isinstance(task.get("title"), str)
                and isinstance(task.get("done"), bool)
            ):
                raise ValueError

        return tasks
    except (json.JSONDecodeError, OSError, ValueError):
        print("경고: 저장 파일을 읽을 수 없어 빈 목록으로 시작합니다.")
        return []


def save_tasks(tasks: list[dict], file_path: Path = DATA_FILE) -> None:
    """할 일 목록을 JSON 파일에 저장합니다."""
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def add_task(tasks: list[dict], title: str) -> dict:
    """새 할 일을 목록에 추가하고 추가된 항목을 반환합니다."""
    title = title.strip()
    if not title:
        raise ValueError("할 일 내용은 비워 둘 수 없습니다.")

    next_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {"id": next_id, "title": title, "done": False}
    tasks.append(new_task)
    return new_task


def complete_task(tasks: list[dict], task_id: int) -> bool:
    """해당 번호의 할 일을 완료 상태로 바꿉니다."""
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def delete_task(tasks: list[dict], task_id: int) -> bool:
    """해당 번호의 할 일을 목록에서 삭제합니다."""
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True
    return False


def show_tasks(tasks: list[dict]) -> str:
    """화면에 표시할 할 일 목록 문자열을 만듭니다."""
    if not tasks:
        return "등록된 할 일이 없습니다."

    lines = ["\n[할 일 목록]"]
    for task in tasks:
        status = "완료" if task["done"] else "진행 중"
        lines.append(f"{task['id']}. [{status}] {task['title']}")
    return "\n".join(lines)


def input_task_id(message: str) -> int | None:
    """할 일 번호를 입력받고 정수가 아니면 None을 반환합니다."""
    try:
        return int(input(message))
    except ValueError:
        print("숫자로 된 할 일 번호를 입력해 주세요.")
        return None


def print_menu() -> None:
    """메인 메뉴를 출력합니다."""
    print("\n=== 할 일 관리 프로그램 ===")
    print("1. 할 일 추가")
    print("2. 전체 조회")
    print("3. 완료 처리")
    print("4. 할 일 삭제")
    print("0. 종료")


def main() -> None:
    """사용자가 종료할 때까지 메뉴를 반복 실행합니다."""
    tasks = load_tasks()

    while True:
        print_menu()
        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            title = input("추가할 할 일을 입력하세요: ")
            try:
                new_task = add_task(tasks, title)
                save_tasks(tasks)
                print(f"'{new_task['title']}' 할 일을 추가했습니다.")
            except ValueError as error:
                print(error)

        elif choice == "2":
            print(show_tasks(tasks))

        elif choice == "3":
            task_id = input_task_id("완료할 할 일 번호를 입력하세요: ")
            if task_id is None:
                continue
            if complete_task(tasks, task_id):
                save_tasks(tasks)
                print("할 일을 완료 처리했습니다.")
            else:
                print("해당 번호의 할 일이 없습니다.")

        elif choice == "4":
            task_id = input_task_id("삭제할 할 일 번호를 입력하세요: ")
            if task_id is None:
                continue
            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("할 일을 삭제했습니다.")
            else:
                print("해당 번호의 할 일이 없습니다.")

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break

        else:
            print("0부터 4까지의 메뉴 번호를 입력해 주세요.")


if __name__ == "__main__":
    main()
