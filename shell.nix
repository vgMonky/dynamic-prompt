{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.setuptools
  ];

  shellHook = ''
    # Create a virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
      python -m venv venv
    fi
    
    # Activate the virtual environment
    source venv/bin/activate
    
    # Install the package in editable mode
    pip install -e .
    
    echo "Dynamic Prompt development environment activated!"
  '';
}
