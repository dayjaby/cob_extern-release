^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package libpcan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.5.1 (2014-03-19)
------------------
* add changelogs
* Updatad libcan-7.9 installation and cleand some files.
* missing builddep
* added missing builddep
* changed copy deps
* Added another include and some more gefrickel
* Added include files for cmake.
* gefrickel ported to cmake
* added patch for libpcan to compile with Linux kernel >=3.4
* fixing runtime linking errors by introducing library versions
* cob_extern is now cob_gefrickel :) did some cmake foo to be compatible to catkin
* Catkinized version of stack.
  Needs checking of build flags in cob_drivers.
  Also includes updating of libphidgets to 2.1.8 for newer boards.
* using tarball from willow server
* Merge branch 'master' of github.com:ipa-nhg/cob_extern
* Updated libpcan to driver 7.6
* add CMakeLists.txt
* Fixed errors in installation script
* Modification in pcan installation script
* add libpopt to rosdep
* fuerte migration
* activated dongle support for peaksys driver
* update manifests
* added md5sum file
* changed . to -
* updated to pcan 6.24 on wg servers
* updated pcan version to 6.24
* using wg tarballs
* using tarball from wg for peak
* cleanup in cob_extern
* update documentation
* libpcan install now with insmod, modprobe and NO_NETDEV_SUPPORT
* additional include export
* IniFiles are passed via arguments in base_drive_chain
* restructure from cob3 to cob
* Merge branch 'master' of git@github.com:ipa320/care-o-bot into review
* renamed to general cob packages
* Contributors: Alexander Bubeck, Denis Štogl, Tobias Fromm, abubeck, cob, ipa, ipa-fmw, ipa-nhg, ipa320-cob3-6