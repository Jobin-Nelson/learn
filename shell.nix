{
  pkgs ? import <nixpkgs> { },
}:
pkgs.mkShell {
  packages = with pkgs; [
    python314
    pyright
    uv
    ruff
    python313Packages.debugpy
  ];
}
