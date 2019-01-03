from cx_Freeze import setup, Executable

setup(
    name = "votre_programme",
    version = "1",
    description = "Votre programme",
    executables = [Executable("start.py")],
)
