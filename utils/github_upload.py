from github import Github
from uuid import uuid4
from setting import settings

g = Github(settings.GITHUB_KEY)
repo = g.get_repo(settings.GITHUB_REPO)

def upload_image(image_bytes: bytes, extension: str):
    filename = f"{uuid4()}.{extension}"

    repo.create_file(
        path="images/"+filename,
        message=f"upload {filename}",
        content=image_bytes
    )

    return filename