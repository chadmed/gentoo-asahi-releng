#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-only
# Gentoo Asahi release builder

: ${BASEDIR:="/var/tmp/catalyst"}
: ${BUILDDIR:="${BASEDIR}/builds"}
: ${VER:=$(date +'%Y%m%d')}
: ${GENTOO_MIRROR:="https://mirror.aarnet.edu.au/pub/gentoo/"}

echo "Trying to enter ${BASEDIR}..."
cd "${BASEDIR}"

echo "Cleaning out ${BASEDIR}..."
#rm -rf "${BASEDIR}"/*

echo "Cloning Gentoo Asahi releng files..."
git clone https://github.com/chadmed/gentoo-asahi-releng \
    --branch=asahi \
    --depth=1 \
    --quiet \
    "${BASEDIR}/releng"

echo "Setting up ::gentoo repo"
mkdir "${BASEDIR}"/repos
git clone https://github.com/gentoo/gentoo.git \
    --depth=1 \
    --bare \
    -c gc.reflogExpire=0 \
    -c gc.reflogExpireUnreachable=0 \
    -c gc.rerereresolved=0 \
    -c gc.rerereunresolved=0 \
    -c gc.pruneExpire=now \
    --branch=master  \
    --quiet \
    "${BASEDIR}/repos/gentoo.git"
catalyst --snapshot master

echo "Cloning ::asahi overlay"
git clone https://github.com/chadmed/asahi-overlay \
    --quiet \
    "${BASEDIR}/asahi-overlay"

echo "Getting latest stage3 from Gentoo Mirror..."
mkdir "${BASEDIR}"/builds
stage3_line=$(curl -L "${GENTOO_MIRROR}/releases/arm64/autobuilds/current-stage3-arm64-openrc/latest-stage3-arm64-openrc.txt" | grep "stage3")
stage3_path="${BASEDIR}/builds/${stage3_line% *}"
curl -L "${GENTOO_MIRROR}/releases/arm64/autobuilds/current-stage3-arm64-openrc/${stage3_line% *}" \
    -o "${stage3_path}" -q

echo "Setting up spec files for build..."
cp "${BASEDIR}/releng/releases/specs/arm64/"*.spec "${BASEDIR}/."
echo "    Setting version timestamp to ${VER}"
sed -i "s/@TIMESTAMP@/${VER}/g" "${BASEDIR}"/*.spec
echo "    Setting ::gentoo snapshot to master"
sed -i "s/@TREEISH@/master/g" "${BASEDIR}"/*.spec
echo "    Setting stage3 path"
sed -i "s+@STAGE3_PATH@+${stage3_line% *}+g" "${BASEDIR}"/*.spec
echo "    Setting releng repo directory"
sed -i "s+@REPO_DIR@+${BASEDIR}/releng+g" "${BASEDIR}"/*.spec
echo "    Setting asahi-overlay directory"
sed -i "s+@ASAHIOVERLAY@+${BASEDIR}/asahi-overlay+g" "${BASEDIR}"/*.spec

echo "Building stage1..."
catalyst -f installcd-stage1.spec

echo "Building stage2 ISO..."
catalyst -f installcd-stage2-minimal.spec
