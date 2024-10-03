{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.setuptools
    python3Packages.wheel
  ];

  shellHook = ''
    echo "Welcome to the dynamic-prompt development environment!"
    echo "Python version: $(python --version)"
  '';
}
