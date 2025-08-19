{ pkgs }: {
  deps = [
    pkgs.openssh_gssapi
    pkgs.u-root-cmds
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.setuptools
    pkgs.python312Packages.wheel
    pkgs.python312Packages.fastapi
    pkgs.python312Packages.uvicorn
    pkgs.python312Packages.httpx
    pkgs.python312Packages.openai
    pkgs.python312Packages.python-dotenv
    pkgs.python312Packages.structlog
    pkgs.python312Packages.tenacity
    pkgs.python312Packages.pydantic
    pkgs.python312Packages.pydantic-settings
    pkgs.python312Packages.aiosqlite
    pkgs.python312Packages.cachetools
    pkgs.uv
  ];
}
