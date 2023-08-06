# -*- coding: utf-8 -*-

import os
import shutil

from preview_generator.manager import PreviewManager

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = "/tmp/preview-generator-tests/cache"
IMAGE_FILE_PATH = os.path.join(CURRENT_DIR, "the_text.txt")
IMAGE_FILE_PATH_NO_EXTENSION = os.path.join(CURRENT_DIR, "the_text_no_extension")  # nopep8


def setup_function(function):
    shutil.rmtree(CACHE_DIR, ignore_errors=True)


def test_text_to_jpeg():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    image_file_path = IMAGE_FILE_PATH
    assert manager.has_jpeg_preview(file_path=image_file_path) is True
    path_to_file = manager.get_jpeg_preview(file_path=image_file_path, force=True)
    assert os.path.exists(path_to_file) is True
    assert os.path.getsize(path_to_file) > 0


def test_to_pdf():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    image_file_path = IMAGE_FILE_PATH
    assert manager.has_jpeg_preview(file_path=image_file_path) is True
    path_to_file = manager.get_pdf_preview(file_path=image_file_path, force=True)
    assert os.path.exists(path_to_file) is True


def test_page_number():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    page_number = manager.get_page_nb(file_path=IMAGE_FILE_PATH)
    assert page_number == 1


def test_to_pdf_no_extension():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    image_file_path = IMAGE_FILE_PATH_NO_EXTENSION
    assert manager.has_jpeg_preview(file_path=image_file_path) is True
    path_to_file = manager.get_pdf_preview(file_path=image_file_path, force=True)
    assert os.path.exists(path_to_file) is True


def test_to_pdf_no_extension_extension_forced():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    image_file_path = IMAGE_FILE_PATH_NO_EXTENSION
    assert manager.has_pdf_preview(file_path=image_file_path, file_ext=".txt") is True
    path_to_file = manager.get_pdf_preview(file_path=image_file_path, force=True, file_ext=".txt")
    assert os.path.exists(path_to_file) is True


def test_to_jpeg_no_extension():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    image_file_path = IMAGE_FILE_PATH_NO_EXTENSION
    assert manager.has_jpeg_preview(file_path=image_file_path) is True
    path_to_file = manager.get_jpeg_preview(file_path=image_file_path, force=True)
    assert os.path.exists(path_to_file) is True


def test_to_jpeg_no_extension_extension_forced():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    image_file_path = IMAGE_FILE_PATH_NO_EXTENSION
    assert manager.has_jpeg_preview(file_path=image_file_path, file_ext=".txt") is True
    path_to_file = manager.get_jpeg_preview(file_path=image_file_path, force=True, file_ext=".txt")
    assert os.path.exists(path_to_file) is True


def test_page_number__no_extension():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    page_number = manager.get_page_nb(file_path=IMAGE_FILE_PATH_NO_EXTENSION)
    assert page_number == 1


def test_page_number__extension_forced():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    page_number = manager.get_page_nb(file_path=IMAGE_FILE_PATH_NO_EXTENSION, file_ext=".txt")
    assert page_number == 1


def test_to_text():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    assert manager.has_text_preview(file_path=IMAGE_FILE_PATH) is True
    manager.get_text_preview(file_path=IMAGE_FILE_PATH, force=True)
    # TODO - G.M - 2018-11-06 - To be completed


def test_to_json():
    manager = PreviewManager(cache_folder_path=CACHE_DIR, create_folder=True)
    assert manager.has_json_preview(file_path=IMAGE_FILE_PATH) is True
    manager.get_json_preview(file_path=IMAGE_FILE_PATH, force=True)
    # TODO - G.M - 2018-11-06 - To be completed
