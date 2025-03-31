import os
import shutil
import uuid
import zipfile
import tempfile
from pathlib import Path
from urllib.parse import urlparse

from fastapi import requests, UploadFile
TMP_DIR = Path("/tmp_uploads")

def unzip_folder(zip_path):
    zip_path = Path(zip_path)
    if not zip_path.exists():
        raise FileNotFoundError(f"Zip file not found: {zip_path}")

    # Use a local directory (tmp_uploads) instead of /data/tmp_uploads
    base_tmp_dir = Path("tmp_uploads")
    os.makedirs(base_tmp_dir, exist_ok=True)

    # If the file is not a valid zip file, simply move it into the temporary directory
    if not zipfile.is_zipfile(zip_path):
        temp_dir = Path(tempfile.mkdtemp(dir=base_tmp_dir))
        temp_file_path = temp_dir / zip_path.name
        zip_path.rename(temp_file_path)
        return str(temp_file_path), [temp_file_path.name]

    # For a valid zip file, create a temporary directory to extract the contents
    extract_to = Path(tempfile.mkdtemp(dir=base_tmp_dir))
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
        file_names = zip_ref.namelist()
    return str(extract_to), file_names


def is_url(path_or_url):
    """Check if the provided string is a URL."""
    if not isinstance(path_or_url, str):
        return False
    try:
        result = urlparse(path_or_url)
        return all([result.scheme, result.netloc])
    except:
        return False


def is_upload_file(obj):
    """Check if the object is a FastAPI UploadFile."""
    return isinstance(obj, UploadFile)


def save_upload_file(upload_file):
    """Save an uploaded file and return the path."""
    file_path = TMP_DIR / f"upload_{str(uuid.uuid4())[:8]}_{upload_file.filename}"

    try:
        # Read the content and save it
        content = upload_file.file.read()
        with open(file_path, 'wb') as f:
            f.write(content)

        # Reset the file pointer for potential reuse
        upload_file.file.seek(0)

        return file_path
    except Exception as e:
        raise Exception(f"Error saving uploaded file: {str(e)}")


def download_file(url):
    """Download a file from a URL to a temporary location and return its path."""
    # Create a temporary file with the correct extension
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path) or f"downloaded_file_{str(uuid.uuid4())[:8]}"

    # Ensure tmp directory exists
    os.makedirs(TMP_DIR, exist_ok=True)

    download_path = TMP_DIR / f"download_{str(uuid.uuid4())[:8]}_{filename}"

    try:
        # Download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(download_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return download_path
    except PermissionError:
        raise Exception(f"Permission denied when writing to {download_path}. Check directory permissions.")
    except Exception as e:
        raise Exception(f"Error downloading file: {str(e)}")


def managed_file_upload(file_input, TMP_DIR=None):
    """
    Enhanced context manager that processes a file input which can be:
    - A path to a file (string)
    - A URL to download (string)
    - A FastAPI UploadFile object

    Args:
        file_input: File path, URL, or UploadFile object

    Yields:
        tuple: (directory path, list of filenames)
    """
    temp_download = None
    temp_upload = None
    output_dir = None
    filenames = []

    try:
        # Case 1: URL handling
        if is_url(file_input):
            try:
                temp_download = download_file(file_input)
                file_path = temp_download
            except Exception as e:
                yield str(e), []
                return

        # Case 2: UploadFile handling
        elif is_upload_file(file_input):
            try:
                temp_upload = save_upload_file(file_input)
                file_path = temp_upload
            except Exception as e:
                yield str(e), []
                return

        # Case 3: File path handling
        else:
            file_path = Path(file_input)

        # Rest of your existing code for processing the file
        session_id = str(uuid.uuid4())[:8]
        os.makedirs(TMP_DIR, exist_ok=True)

        if zipfile.is_zipfile(file_path):
            # Handle ZIP file
            output_dir = TMP_DIR / f"zip_{session_id}"
            os.makedirs(output_dir, exist_ok=True)

            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(output_dir)
                filenames = zip_ref.namelist()
        else:
            # Handle single file
            output_dir = TMP_DIR
            dest_path = output_dir / f"{session_id}_{os.path.basename(str(file_path))}"
            shutil.copy2(file_path, dest_path)
            filenames = [os.path.basename(str(dest_path))]

        yield str(output_dir), filenames

    finally:
        # Clean up temporary files
        for temp_file in [temp_download, temp_upload]:
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)

        # Clean up extracted/copied files
        if output_dir and output_dir.exists() and output_dir != TMP_DIR:
            shutil.rmtree(output_dir)
        elif output_dir == TMP_DIR:
            for filename in filenames:
                file_to_remove = output_dir / filename
                if file_to_remove.exists():
                    os.remove(file_to_remove)


def process_uploaded_file(file_path_or_url):
    """
    Processes uploaded files or URLs and returns paths without automatic cleanup.

    Args:
        file_path_or_url: Path to the file or URL to download

    Returns:
        tuple: (directory path, list of filenames)
    """
    temp_download = None

    try:
        # Handle URL if provided
        if is_url(file_path_or_url):
            try:
                temp_download = download_file(file_path_or_url)
                file_path = temp_download
            except Exception as e:
                return str(e), []
        else:
            file_path = Path(file_path_or_url)

        # Ensure tmp directory exists
        os.makedirs(TMP_DIR, exist_ok=True)

        # Generate a unique session ID
        session_id = str(uuid.uuid4())[:8]

        if zipfile.is_zipfile(file_path):
            # Handle ZIP file
            output_dir = TMP_DIR / f"zip_{session_id}"
            os.makedirs(output_dir, exist_ok=True)

            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(output_dir)
                filenames = zip_ref.namelist()

            return str(output_dir), filenames
        else:
            # Handle single file
            dest_path = TMP_DIR / f"{session_id}_{os.path.basename(str(file_path))}"
            shutil.copy2(file_path, dest_path)

            return str(TMP_DIR), [os.path.basename(str(dest_path))]
    finally:
        # Clean up downloaded file if needed but not the processed result
        if temp_download and os.path.exists(temp_download):
            os.remove(temp_download)


def check_disk_space():
    """Check if there's enough disk space available."""
    import shutil
    stats = shutil.disk_usage("/tmp")
    free_mb = stats.free / (1024 * 1024)
    if free_mb < 50:  # Less than 50MB free
        return False
    return True