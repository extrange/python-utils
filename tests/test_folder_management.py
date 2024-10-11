from pathlib import Path

from python_utils.folder_management import (
    clear_directory,
    create_directory,
    delete_directory,
)


class TestFolderManagement:
    def test_create_directory(self, tmp_path: Path):
        """Test creating a directory."""
        new_dir = tmp_path / "new_dir"
        create_directory(new_dir)
        assert new_dir.exists()
        assert new_dir.is_dir()

    def test_clear_directory(self, tmp_path: Path):
        """Test clearing a directory."""
        sub_dir = tmp_path / "sub_dir"
        sub_dir.mkdir()
        (sub_dir / "file.txt").write_text("test")

        assert sub_dir.exists()
        assert (sub_dir / "file.txt").exists()
        clear_directory(tmp_path)
        assert not sub_dir.exists()

    def test_delete_directory(self, tmp_path: Path):
        """Test deleting a directory."""
        delete_directory(tmp_path)
        assert not tmp_path.exists()

    def test_delete_nonexistent_directory(self, tmp_path: Path):
        """Test deleting a non-existent directory."""
        nonexistent_dir = tmp_path / "nonexistent"

        # Should not raise an error
        delete_directory(nonexistent_dir)
