{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  buildInputs = [
    pkgs.poetry
    pkgs.stdenv.cc.cc.lib
  ];
  shellHook = ''
  export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib
  '';
}
