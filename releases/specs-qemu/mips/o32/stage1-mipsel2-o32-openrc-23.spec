subarch: mipsel2
target: stage1
version_stamp: openrc-@TIMESTAMP@
interpreter: /usr/bin/qemu-mipsel
rel_type: 23.0-default
profile: default/linux/mips/23.0/mipsel/o32
snapshot_treeish: @TREEISH@
source_subpath: 23.0-default/stage3-mipsel2-openrc-latest
compression_mode: pixz
decompressor_search_order: xz
update_seed: yes
update_seed_command: -uDN @world
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
