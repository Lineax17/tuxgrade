# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.1.0] - Unreleased

### Added
- Arch Linux support (Pacman, Paru, Yay)

### Changed
- Removed silent/verbose mode toggle — always shows live output
- Removed `--verbose`/`-l`/`--log` CLI flag
- Removed spinner animation (`run_with_spinner`)

## [3.0.1] - 2026-02-16

### Added
- GPG repository signing with RSA 4096-bit
- Automated build and release pipeline via GitHub Actions
- Signed DEB and RPM repos

### Changed
- Improved repository security with cryptographic signatures

## [3.0.0] - 2026-02-07

### Changed
- Rebranding from "fedora-update" to "tuxgrade"
- Multi-distribution support added:
  - Debian
  - Linux Mint
  - Ubuntu
  - Pop!_OS
  - Zorin OS
  - Fedora
  - RHEL
  - Rocky Linux
  - AlmaLinux

## [2.0.1] - 2026-01-03

### Fixed
- Minor visual issues in terminal output
- Removed DNF5 hardlock to enable DNF4 support (tested with DNF 4.19 on Fedora 40)

## [2.0.0] - 2025-12-27

### Changed
- Complete Python rewrite for better maintainability
- Improved error handling and logging
- Modular architecture for better code organization

### Added
- Modern Python packaging with pyproject.toml
- Comprehensive test suite
- API documentation

[Unreleased]: https://github.com/Lineax17/tuxgrade/compare/v3.0.0...HEAD
[3.0.0]: https://github.com/Lineax17/tuxgrade/compare/v2.0.1...v3.0.0
[2.0.1]: https://github.com/Lineax17/tuxgrade/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/Lineax17/tuxgrade/releases/tag/v2.0.0
