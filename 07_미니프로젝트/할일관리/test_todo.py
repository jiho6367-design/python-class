"""할 일 관리 프로그램의 기능을 확인하는 테스트입니다."""

import json
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from todo import add_task, complete_task, delete_task, load_tasks, save_tasks, show_tasks


class TodoTest(unittest.TestCase):
    def test_add_task_assigns_unique_id(self) -> None:
        tasks = [{"id": 2, "title": "기존 할 일", "done": False}]

        new_task = add_task(tasks, "  파이썬 과제 제출  ")

        self.assertEqual(new_task, {"id": 3, "title": "파이썬 과제 제출", "done": False})

    def test_add_task_rejects_empty_title(self) -> None:
        with self.assertRaises(ValueError):
            add_task([], "   ")

    def test_save_and_load_tasks(self) -> None:
        tasks = [{"id": 1, "title": "강의 복습", "done": False}]

        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "tasks.json"
            save_tasks(tasks, file_path)

            self.assertEqual(load_tasks(file_path), tasks)

    def test_complete_and_delete_task(self) -> None:
        tasks = [
            {"id": 1, "title": "책 읽기", "done": False},
            {"id": 2, "title": "산책하기", "done": False},
        ]

        self.assertTrue(complete_task(tasks, 1))
        self.assertTrue(tasks[0]["done"])
        self.assertFalse(complete_task(tasks, 99))
        self.assertTrue(delete_task(tasks, 2))
        self.assertFalse(delete_task(tasks, 99))
        self.assertEqual(len(tasks), 1)

    def test_show_tasks(self) -> None:
        tasks = [
            {"id": 1, "title": "과제하기", "done": False},
            {"id": 2, "title": "제출하기", "done": True},
        ]

        result = show_tasks(tasks)

        self.assertIn("1. [진행 중] 과제하기", result)
        self.assertIn("2. [완료] 제출하기", result)
        self.assertEqual(show_tasks([]), "등록된 할 일이 없습니다.")

    def test_corrupted_file_starts_with_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "tasks.json"
            file_path.write_text("{잘못된 JSON", encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                tasks = load_tasks(file_path)

            self.assertEqual(tasks, [])
            self.assertIn("경고", output.getvalue())

    def test_invalid_task_structure_starts_with_empty_list(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            file_path = Path(directory) / "tasks.json"
            file_path.write_text(json.dumps([{"title": "번호 없음"}]), encoding="utf-8")
            output = StringIO()

            with redirect_stdout(output):
                tasks = load_tasks(file_path)

            self.assertEqual(tasks, [])
            self.assertIn("경고", output.getvalue())


if __name__ == "__main__":
    unittest.main()
