from typing import Optional
from typing import Type

from fastapi import HTTPException
from starlette import status

from api import schema
from api.consts import JSONAPI_CONTENT_TYPE
from api.errors import BadRequest
import os
import zipfile

from framework.dirs import DIR_DOWNLOAD


def validate_content_type(content_type: Optional[str]):
    if content_type != JSONAPI_CONTENT_TYPE:
        supported_cts = sorted([JSONAPI_CONTENT_TYPE])
        errmsg = (
            f"Unsupported content type {content_type}."
            f" Supported content types: {supported_cts}."
        )

        raise BadRequest(errmsg)


def get_or_404(model: Type, pk: int):
    if pk:
        obj = model.objects.filter(pk=pk).first()
        if obj:
            return obj

    errors = schema.ErrorsJsonApi(
        errors=[f"object of {model.__name__} with pk={pk} not found"]
    )
    errors.meta.ok = False

    raise HTTPException(
        detail=errors.dict(),
        status_code=status.HTTP_404_NOT_FOUND,
    )


def update_normal_fields(orm_obj, schema_obj, *, exclude_unset=False) -> None:
    kw = schema_obj.dict(exclude_unset=exclude_unset)

    for name, value in kw.items():
        if name == "id":
            continue
        setattr(orm_obj, name, value)

    orm_obj.save()


def generate_settings_file(server: str, user_id: str) -> str:
    settings_file = os.path.join(DIR_DOWNLOAD, f"{user_id}")
    os.makedirs(settings_file, exist_ok=True)
    settings_file = os.path.join(settings_file, "PostEditor.ini")
    with open(settings_file, "w") as fd:
        fd.write(f"[General]\n")
        fd.write(f"server={server}\n")
        fd.write(f"author_id={user_id}")
    return settings_file


def zip_files(filenames: list, user_id: int) -> str:
    zip_filename = os.path.join(DIR_DOWNLOAD, f"{user_id}", "PostEditor.zip")
    with zipfile.ZipFile(zip_filename, "w") as zf:
        for file_path in filenames:
            zf.write(file_path, os.path.basename(file_path))
    return zip_filename
