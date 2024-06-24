Gentoo Asahi Release Engineering Builds
---------------------------------
Semi-official Gentoo Asahi Releng files

Use this repo to build bootable installation media for Apple Silicon Macs.

To use these builds, you need Gentoo's Catalyst tool.

## Quirks
* The dist-kernel version string doesn't match what equery returns. You will need to move the `/lib/modules/${WHATEVER}` folder
  and resume during the stage2 build until this is fixed in asahi-overlay.
