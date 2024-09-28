from pathlib import Path
import shutil
import os
from python_utils.folder_management import create_directory, delete_directory, clear_directory

class TestFolderManagement:
    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = Path("temp_test_dir")
        self.test_dir.mkdir(exist_ok=True)

    def tearDown(self):
        """Remove the temporary directory after tests."""
        if self.test_dir.exists() and self.test_dir.is_dir():
            shutil.rmtree(self.test_dir)

    def test_create_directory(self):
        """Test creating a directory."""
        new_dir = self.test_dir / "new_dir"
        create_directory(new_dir)
        self.assertTrue(new_dir.exists())
        self.assertTrue(new_dir.is_dir())

    def test_clear_directory(self):
        """Test clearing a directory."""
        sub_dir = self.test_dir / "sub_dir"
        sub_dir.mkdir()
        (sub_dir / "file.txt").write_text("test")

        self.assertTrue(sub_dir.exists())
        self.assertTrue((sub_dir / "file.txt").exists())
        clear_directory(self.test_dir)
        self.assertFalse(sub_dir.exists())

    def test_delete_directory(self):
        """Test deleting a directory."""
        create_directory(self.test_dir)
        self.assertTrue(self.test_dir.exists())

        delete_directory(self.test_dir)
        self.assertFalse(self.test_dir.exists())

    def test_delete_nonexistent_directory(self):
        """Test deleting a non-existent directory."""
        nonexistent_dir = self.test_dir / "nonexistent"
        delete_directory(nonexistent_dir)  # Should not raise an error

