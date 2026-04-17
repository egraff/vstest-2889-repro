import argparse
import glob
import shutil

from pathlib import Path
from string import Template


SLNX_TEMPLATE = Template(
    """
<Solution>
  <Folder Name="/Solution Items/">
    <File Path="NuGet.Config" />
  </Folder>
  <Folder Name="/src/">$src_projects
  </Folder>
  <Folder Name="/tests/">
    <Project Path="tests/VSTestIssueReproTests.csproj" />
  </Folder>
</Solution>
"""
)


def is_dir_empty(dirpath: Path):
    try:
        next(dirpath.iterdir())
    except StopIteration:
        return True

    return False


def rmtree(dirpath: Path):
    for child in dirpath.iterdir():
        if child.is_dir():
            rmtree(child)
        else:
            if child.name != ".gitkeep":
                child.unlink()

    if is_dir_empty(dirpath):
        dirpath.rmdir()


def generate_repro(num_projects: int):
    orig_dir = Path("repro")
    assert orig_dir.exists()

    gen_dir = Path("generated_repro")
    rmtree(gen_dir)
    gen_dir.mkdir(exist_ok=True)

    shutil.copy(orig_dir.joinpath("NuGet.Config"), gen_dir)

    tests_dir = gen_dir.joinpath("tests")
    tests_dir.mkdir(exist_ok=True)

    shutil.copy(
        orig_dir.joinpath("tests").joinpath("VSTestIssueReproTests.csproj"), tests_dir
    )
    shutil.copy(orig_dir.joinpath("tests").joinpath("Tests.cs"), tests_dir)

    src_dir = gen_dir.joinpath("src")
    src_dir.mkdir(exist_ok=True)

    proj_paths = []
    for i in range(num_projects):
        proj_name = f"Src{(i + 1):03}"
        csproj_name = f"{proj_name}.csproj"

        proj_dir = src_dir.joinpath(proj_name)
        proj_dir.mkdir()

        shutil.copy(
            orig_dir.joinpath("src").joinpath("Src001").joinpath("Src001.csproj"),
            proj_dir.joinpath(csproj_name),
        )

        proj_paths.append(f"src/{proj_name}/{proj_name}.csproj")

    slnx_contents = SLNX_TEMPLATE.safe_substitute(
        src_projects="".join([f'\n    <Project Path="{p}" />' for p in proj_paths])
    )
    with open(gen_dir.joinpath("repro.slnx"), "w") as fp:
        fp.write(slnx_contents)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="generate.py", description="Generates a reproduction of the VS test issue"
    )
    parser.add_argument("--num", type=int, default=100)

    args = parser.parse_args()

    generate_repro(args.num)
