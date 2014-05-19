%define with_printer_applet 0
%{?_with_printer_applet: %{expand: %%global with_printer_applet 1}}

%define with_networkmanager 1
%{?_with_networkmanager: %{expand: %%global with_networkmanager 1}}

%define with_drakclock 1
%{?_with_networkmanager: %{expand: %%global with_networkmanager 1}}

%define kdm_version 2.7.2

Summary:	KDE 4 application workspace components
Name:		kdebase4-workspace
Version:	4.11.8
Release:	4
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/kde-workspace-%{version}.tar.xz
Source1:	kde.pam
Source2:	kde-np.pam
Source4:	systemsettings.desktop
Source5:	krandrtray.desktop
Source6:	kdebase-workspace-kdm-%{kdm_version}.tar.bz2
Source8:	kcm_drakclock.desktop
Source9:	omv-startkde
Source10:	rosa-startkde
Source11:	omv-kdm.service
Source12:	rosa-kdm.service
Source20:	%{name}.rpmlintrc
Patch0:		kdebase-workspace-4.5.76-mdv-adopt-ldetect-path.patch
# Use drakclock for time settings, patch from Mageia
Patch1:		kdebase-workspace-4.6.2-mageia-drakclock.patch
# Hide native clock configurator as we have drakclock instead
Patch2:		kde-workspace-4.10.2-hide-default-clock.patch
Patch3:		kdebase-workspace-4.11.0-menu-toptile.patch
# Add checkbox to enable/disable bytecode interpreter in KDE4 font anti-aliasing settings
Patch4:		kde-workspace-4.9.4-fontconfig.patch
# Just a workaround to make sure text box size for OSD is always big enough
Patch5:		kde-workspace-4.11.0-desktop-osd.patch
# Always show icons in pager widget, even if they don't fit window rectangle
Patch6:		kde-workspace-4.10.3-pager-icons.patch
# Fix action labels vertical alignment in Device Notifier applet
Patch7:		kde-workspace-4.10.3-devicenotifier.patch
# Fix screenlocker greeter focus after Alt modifier is pressed (keyboard layout switching etc)
Patch8:		kde-workspace-4.10.3-greeter.patch
# Patch from OpenSUSE, fixes 2 issues:
# * password input dialog was not shown under certain circumstances
#  (kde#327947, kde#329076, bnc#864305)
# * screensaver processes might keep running in background when
#  unlocking the screen (kde#224200, bnc#809835)
Patch9:		kdebase4-workspace-4.11.8-fix-screenlocker-ulock.patch
# Prefer system locale for KDM when reading it from KDM config fails
Patch10:	kde-workspace-4.10.3-fix-kcmkdm-locale.patch
Patch11:	kdebase-workspace-4.2.0-fix_gtkrc_iaora.patch
# Fix screenlocker greeter focus when screensaver is used
Patch12:	kde-workspace-4.11.4-screenlocker-handle-fake-focus.patch
# Use current wallpaper for screenlocker if it's a scaled image
Patch13:	kde-workspace-4.11.4-screenlocker-background.patch
# Don't add activities and launchers to standard panel by default
Patch14:	kde-workspace-4.11.0-default-panel-layout.patch
Patch18:	kdebase-workspace-4.8.95-startup-sound.patch
Patch19:	kdebase-workspace-4.2.1-use-mdvicon.patch
Patch26:	kdebase-workspace-4.11.0-simpleapplet-defaults.patch
# Make it possible to set wallpaper via dbus
# See https://bugs.kde.org/show_bug.cgi?id=217950
Patch27:	kde-workspace-4.11.6-dbus-wallpaper.patch
# See http://quickgit.kde.org/?p=kde-workspace.git&a=commitdiff&h=c1469413f36d4e4cd9dd49e70bc5d660cf2f3c55
# And http://quickgit.kde.org/?p=kde-workspace.git&a=commitdiff&h=dcc70fbb55919ac56ae188ceb3d5bf7b94c2dbcd
# We partially revert it because we need at least deKorator to work
Patch50:	kde-workspace-4.11.3-decorations.patch
Patch100:	kdebase-workspace-4.8.1-hideklipper.patch
Patch101:	kdebase-workspace-4.8.97-klippermenu.patch
Patch104:	kdebase-workspace-4.7.3.fedora-kdm-plymouth.patch
Patch106:	kdebase-workspace-4.11.0-no-hal.patch
# Make systemd 194 handle upower stuff
Patch107:	kde-workspace-4.10.3-powerdevil-systemd.patch

# Backports

# Trunk
# Testing

BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	ieee1284-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	python-kde4-devel
BuildRequires:	prison-devel
BuildRequires:	sasl-devel
BuildRequires:	automoc4
BuildRequires:	bdftopcf
BuildRequires:	imake
BuildRequires:	libxml2-utils
BuildRequires:	qt4-qtdbus
BuildRequires:	xrdb
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(libggadget-1.0)
BuildRequires:	pkgconfig(libggadget-qt-1.0)
BuildRequires:	pkgconfig(libgpsd)
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(lua)
%if %{with_networkmanager}
BuildRequires:	pkgconfig(NetworkManager)
%endif
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xtst)
Requires:	desktop-common-data
Requires:	kdebase4-runtime
Requires:	kde4-windeco-dekorator
Requires:	mandriva-kde-translation
Requires:	qt4-qtdbus
Requires:	setxkbmap
Requires:	strigi
Requires:	udisks2
Requires:	xdg-utils
Requires:	xmessage
Requires:	xprop
Requires:	xset
Suggests:	kickoff
Suggests:	klipper
Suggests:	networkmanager
Suggests:	plasma-applet-system-monitor-net
Suggests:	plasma-applet-system-monitor-hwinfo
Suggests:	plasma-applet-system-monitor-hdd
Suggests:	plasma-applet-system-monitor-cpu
Suggests:	plasma-applet-system-monitor-temperature
%if %{disttag} == "omv"
Requires:	homerun
%else
Suggests:	rosapanel
%endif
Conflicts:	kdm < 2:4.10.2-4
Obsoletes:	kdebase4-workspace-googlegadgets < 2:4.11.0
Obsoletes:	%{_lib}solidcontrolifaces4 < 2:4.11.0
Obsoletes:	%{_lib}solidcontrol4 < 2:4.11.0
Obsoletes:	%{_lib}kwinnvidiahack4 < 2:4.11.0

%description
This package contains the KDE 4 application workspace components.

%files
%{_sysconfdir}/X11/wmsession.d/*
%{_sysconfdir}/profile.d/70kde4.sh
%if %{with_printer_applet}
%{_kde_bindir}/printer-applet
%{_kde_appsdir}/printer-applet
%endif
%{_kde_sysconfdir}/dbus-1/system.d/org.kde.fontinst.conf
%{_kde_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmclock.conf
%{_kde_sysconfdir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_kde_sysconfdir}/ksysguarddrc
%{_kde_bindir}/kaccess
%{_kde_bindir}/kapplymousetheme
%{_kde_bindir}/kblankscrn.kss
%{_kde_bindir}/kcheckrunning
%{_kde_bindir}/kcminit
%{_kde_bindir}/kcminit_startup
%{_kde_bindir}/kdostartupconfig4
%{_kde_bindir}/kfontinst
%{_kde_bindir}/kfontview
%{_kde_bindir}/kmenuedit
%{_kde_bindir}/krandom.kss
%{_kde_bindir}/krandrstartup
%{_kde_bindir}/krandrtray
%{_kde_bindir}/krdb
%{_kde_bindir}/krunner
%{_kde_bindir}/ksmserver
%{_kde_bindir}/ksplashsimple
%{_kde_bindir}/ksplashx
%{_kde_bindir}/ksplashx_scale
%{_kde_bindir}/ksplashqml
%{_kde_bindir}/kstartupconfig4
%{_kde_bindir}/ksysguard
%{_kde_bindir}/ksysguardd
%{_kde_bindir}/ksystraycmd
%{_kde_bindir}/kwin*
%{_kde_bindir}/oxygen-demo
%{_kde_bindir}/oxygen-settings
%{_kde_bindir}/plasma-desktop
%{_kde_bindir}/plasma-netbook
%{_kde_bindir}/plasma-overlay
%{_kde_bindir}/plasma-windowed
%{_kde_bindir}/solid-action-desktop-gen
%{_kde_bindir}/startkde
%{_kde_bindir}/oxygen-shadow-demo
%{_kde_bindir}/systemsettings
%{_kde_libdir}/kconf_update_bin/*
%{_kde_libdir}/kde4/imports
%{_kde_libdir}/kde4/classic_mode.so
%{_kde_libdir}/kde4/fontthumbnail.so
%{_kde_libdir}/kde4/icon_mode.so
%{_kde_libdir}/kde4/ion_bbcukmet.so
%{_kde_libdir}/kde4/ion_envcan.so
%{_kde_libdir}/kde4/ion_noaa.so
%{_kde_libdir}/kde4/ion_wettercom.so
%{_kde_libdir}/kde4/kcm_access.so
%{_kde_libdir}/kde4/kcm_autostart.so
%{_kde_libdir}/kde4/kcm_bell.so
%{_kde_libdir}/kde4/kcm_clock.so
%{_kde_libdir}/kde4/kcm_colors.so
%{_kde_libdir}/kde4/kcm_cursortheme.so
%{_kde_libdir}/kde4/kcm_desktoppaths.so
%{_kde_libdir}/kde4/kcm_desktoptheme.so
%{_kde_libdir}/kde4/kcm_display.so
%{_kde_libdir}/kde4/kcm_fontinst.so
%{_kde_libdir}/kde4/kcm_fonts.so
%{_kde_libdir}/kde4/kcm_hotkeys.so
%{_kde_libdir}/kde4/kcm_input.so
%{_kde_libdir}/kde4/kcm_joystick.so
%{_kde_libdir}/kde4/kcm_keyboard.so
%{_kde_libdir}/kde4/kcm_keys.so
%{_kde_libdir}/kde4/kcm_krunner_kill.so
%{_kde_libdir}/kde4/kcm_ksplashthemes.so
%{_kde_libdir}/kde4/kcm_kwin4_effect_builtins.so
%{_kde_libdir}/kde4/kcm_kwin4_genericscripted.so
%{_kde_libdir}/kde4/kwin4_effect_gles_builtins.so
%{_kde_libdir}/kde4/kcm_kwincompositing.so
%{_kde_libdir}/kde4/kcm_kwindecoration.so
%{_kde_libdir}/kde4/kcm_kwindesktop.so
%{_kde_libdir}/kde4/kcm_kwinoptions.so
%{_kde_libdir}/kde4/kcm_kwinrules.so
%{_kde_libdir}/kde4/kcm_kwinscreenedges.so
%{_kde_libdir}/kde4/kcm_kwin_scripts.so
%{_kde_libdir}/kde4/kcm_kwintabbox.so
%{_kde_libdir}/kde4/kcm_launch.so
%{_kde_libdir}/kde4/kcm_randr.so
%{_kde_libdir}/kde4/kcm_screensaver.so
%{_kde_libdir}/kde4/kcm_smserver.so
%{_kde_libdir}/kde4/kcm_solid_actions.so
%{_kde_libdir}/kde4/kcm_standard_actions.so
%{_kde_libdir}/kde4/kcm_style.so
%{_kde_libdir}/kde4/kcm_workspaceoptions.so
%{_kde_libdir}/kde4/kded_freespacenotifier.so
%{_kde_libdir}/kde4/kded_kephal.so
%{_kde_libdir}/kde4/kded_keyboard.so
%{_kde_libdir}/kde4/kded_khotkeys.so
%{_kde_libdir}/kde4/kded_kwrited.so
%{_kde_libdir}/kde4/kded_randrmonitor.so
%{_kde_libdir}/kde4/kded_statusnotifierwatcher.so
%{_kde_libdir}/kde4/keyboard_layout_widget.so
%{_kde_libdir}/kde4/kfontviewpart.so
%{_kde_libdir}/kde4/kio_fonts.so
%{_kde_libdir}/kde4/krunner_bookmarksrunner.so
%{_kde_libdir}/kde4/krunner_calculatorrunner.so
%{_kde_libdir}/kde4/krunner_kill.so
%{_kde_libdir}/kde4/krunner_locations.so
%{_kde_libdir}/kde4/krunner_nepomuksearchrunner.so
%{_kde_libdir}/kde4/krunner_plasma-desktop.so
%{_kde_libdir}/kde4/krunner_recentdocuments.so
%{_kde_libdir}/kde4/krunner_services.so
%{_kde_libdir}/kde4/krunner_sessions.so
%{_kde_libdir}/kde4/krunner_shell.so
%{_kde_libdir}/kde4/krunner_solid.so
%{_kde_libdir}/kde4/krunner_webshortcuts.so
%{_kde_libdir}/kde4/krunner_windowedwidgets.so
%{_kde_libdir}/kde4/krunner_windows.so
%{_kde_libdir}/kde4/kstyle_oxygen_config.so
%{_kde_libdir}/kde4/kwin3_aurorae.so
%{_kde_libdir}/kde4/kwin3_b2.so
%{_kde_libdir}/kde4/kwin3_laptop.so
%{_kde_libdir}/kde4/kwin3_oxygen.so
%{_kde_libdir}/kde4/kwin4_effect_builtins.so
%{_kde_libdir}/kde4/kwin_b2_config.so
%{_kde_libdir}/kde4/kwin_oxygen_config.so
%{_kde_libdir}/kde4/libexec/fontinst
%{_kde_libdir}/kde4/libexec/fontinst_helper
%{_kde_libdir}/kde4/libexec/fontinst_x11
%{_kde_libdir}/kde4/libexec/kcmdatetimehelper
%{_kde_libdir}/kde4/libexec/ksysguardprocesslist_helper
%{_kde_libdir}/kde4/libexec/kwin_killer_helper
%{_kde_libdir}/kde4/libexec/kwin_opengl_test
%{_kde_libdir}/kde4/libexec/kwin_rules_dialog
%{_kde_libdir}/kde4/libexec/kscreenlocker_greet
%{_kde_libdir}/kde4/kded_appmenu.so
%{_kde_libdir}/kde4/kded_ktouchpadenabler.so
%{_kde_libdir}/kde4/plasma-geolocation-gps.so
%{_kde_libdir}/kde4/plasma-geolocation-ip.so
%{_kde_libdir}/kde4/plasma_animator_default.so
%{_kde_libdir}/kde4/plasma_applet_activitybar.so
%{_kde_libdir}/kde4/plasma_applet_clock.so
%{_kde_libdir}/kde4/plasma_applet_currentappcontrol.so
%{_kde_libdir}/kde4/plasma_applet_dig_clock.so
%{_kde_libdir}/kde4/plasma_applet_icon.so
%{_kde_libdir}/kde4/plasma_applet_keyboard.so
%{_kde_libdir}/kde4/plasma_applet_pager.so
%{_kde_libdir}/kde4/plasma_applet_panelspacer_internal.so
%{_kde_libdir}/kde4/plasma_applet_searchbox.so
%{_kde_libdir}/kde4/plasma_applet_sm_hdd_activity.so
%{_kde_libdir}/kde4/plasma_applet_sm_ram.so
%{_kde_libdir}/kde4/plasma_applet_system-monitor.so
%{_kde_libdir}/kde4/plasma_applet_systemtray.so
%{_kde_libdir}/kde4/plasma_applet_tasks.so
%{_kde_libdir}/kde4/plasma_applet_trash.so
%{_kde_libdir}/kde4/plasma_applet_windowlist.so
%{_kde_libdir}/kde4/plasma_appletscriptengine_dashboard.so
%{_kde_libdir}/kde4/plasma_appletscriptengine_webapplet.so
%{_kde_libdir}/kde4/plasma_containment_desktop.so
%{_kde_libdir}/kde4/plasma_containment_netpanel.so
%{_kde_libdir}/kde4/plasma_containment_panel.so
%{_kde_libdir}/kde4/plasma_containment_sal.so
%{_kde_libdir}/kde4/plasma_containment_saverdesktop.so
%{_kde_libdir}/kde4/plasma_containmentactions_applauncher.so
%{_kde_libdir}/kde4/plasma_containmentactions_contextmenu.so
%{_kde_libdir}/kde4/plasma_containmentactions_minimalcontextmenu.so
%{_kde_libdir}/kde4/plasma_containmentactions_paste.so
%{_kde_libdir}/kde4/plasma_containmentactions_switchactivity.so
%{_kde_libdir}/kde4/plasma_containmentactions_switchdesktop.so
%{_kde_libdir}/kde4/plasma_containmentactions_switchwindow.so
%{_kde_libdir}/kde4/plasma_engine_activities.so
%{_kde_libdir}/kde4/plasma_engine_akonadi.so
%{_kde_libdir}/kde4/plasma_engine_applicationjobs.so
%{_kde_libdir}/kde4/plasma_engine_apps.so
%{_kde_libdir}/kde4/plasma_engine_calendar.so
%{_kde_libdir}/kde4/plasma_engine_devicenotifications.so
%{_kde_libdir}/kde4/plasma_engine_dict.so
%{_kde_libdir}/kde4/plasma_engine_executable.so
%{_kde_libdir}/kde4/plasma_engine_favicons.so
%{_kde_libdir}/kde4/plasma_engine_filebrowser.so
%{_kde_libdir}/kde4/plasma_engine_geolocation.so
%{_kde_libdir}/kde4/plasma_engine_hotplug.so
%{_kde_libdir}/kde4/plasma_engine_keystate.so
%{_kde_libdir}/kde4/plasma_engine_metadata.so
%{_kde_libdir}/kde4/plasma_engine_mouse.so
%{_kde_libdir}/kde4/plasma_engine_mpris2.so
%{_kde_libdir}/kde4/plasma_engine_notifications.so
%{_kde_libdir}/kde4/plasma_engine_nowplaying.so
%{_kde_libdir}/kde4/plasma_engine_places.so
%{_kde_libdir}/kde4/plasma_engine_powermanagement.so
%{_kde_libdir}/kde4/plasma_engine_rss.so
%{_kde_libdir}/kde4/plasma_engine_searchlaunch.so
%{_kde_libdir}/kde4/plasma_engine_share.so
%{_kde_libdir}/kde4/plasma_engine_soliddevice.so
%{_kde_libdir}/kde4/plasma_engine_statusnotifieritem.so
%{_kde_libdir}/kde4/plasma_engine_systemmonitor.so
%{_kde_libdir}/kde4/plasma_engine_tasks.so
%{_kde_libdir}/kde4/plasma_engine_time.so
%{_kde_libdir}/kde4/plasma_engine_weather.so
%{_kde_libdir}/kde4/plasma_packagestructure_dashboard.so
%{_kde_libdir}/kde4/plasma_packagestructure_share.so
%{_kde_libdir}/kde4/plasma_packagestructure_web.so
%{_kde_libdir}/kde4/plasma_toolbox_desktoptoolbox.so
%{_kde_libdir}/kde4/plasma_toolbox_nettoolbox.so
%{_kde_libdir}/kde4/plasma_toolbox_paneltoolbox.so
%{_kde_libdir}/kde4/plasma_wallpaper_color.so
%{_kde_libdir}/kde4/plasma_wallpaper_image.so
%{_kde_libdir}/kde4/plugins/gui_platform/libkde.so
%{_kde_libdir}/kde4/plugins/styles/oxygen.so
%{_kde_libdir}/kde4/powerdevilkeyboardbrightnesscontrolaction_config.so
%{_kde_libdir}/kde4/ion_debianweather.so
%{_kde_libdir}/kde4/krunner_activities.so
%{_kde_libdir}/libkdeinit4_*.so
%{_kde_libdir}/strigi/strigita_font.so
%{_kde_applicationsdir}/kfontview.desktop
%{_kde_applicationsdir}/kmenuedit.desktop
%{_kde_applicationsdir}/krandrtray.desktop
%{_kde_applicationsdir}/ksysguard.desktop
%{_kde_applicationsdir}/systemsettings.desktop
%{_kde_applicationsdir}/kdesystemsettings.desktop
%{_kde_appsdir}/color-schemes
%{_kde_appsdir}/desktoptheme
%{_kde_appsdir}/freespacenotifier
%{_kde_appsdir}/kaccess
%{_kde_appsdir}/katepart
%{_kde_appsdir}/kcminput
%{_kde_appsdir}/kcmkeys
%{_kde_appsdir}/kcmstyle
%{_kde_appsdir}/kcmsolidactions
%{_kde_appsdir}/kconf_update/*
%{_kde_appsdir}/kcontrol
%{_kde_appsdir}/kdisplay
%{_kde_appsdir}/kfontinst
%{_kde_appsdir}/kfontview
%{_kde_appsdir}/khotkeys
%{_kde_appsdir}/kmenuedit
%{_kde_appsdir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_kde_appsdir}/ksmserver
%{_kde_appsdir}/ksplash
%{_kde_appsdir}/kstyle
%{_kde_appsdir}/ksysguard
%{_kde_appsdir}/kthememanager
%{_kde_appsdir}/kwin
%{_kde_appsdir}/kwrited
%{_kde_appsdir}/plasma
%{_kde_appsdir}/plasma-desktop
%{_kde_appsdir}/plasma-netbook
%{_kde_appsdir}/solid/*/*.desktop
%{_kde_appsdir}/systemsettings
%{_kde_appsdir}/kcmkeyboard
%{_kde_autostart}/*.desktop
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_configdir}/xcursor.knsrc
%{_kde_configdir}/activities.knsrc
%{_kde_configdir}/aurorae.knsrc
%{_kde_configdir}/background.knsrc
%{_kde_configdir}/colorschemes.knsrc
%{_kde_configdir}/ksplash.knsrc
%{_kde_configdir}/ksysguard.knsrc
%{_kde_configdir}/kwineffect.knsrc
%{_kde_configdir}/kwinscripts.knsrc
%{_kde_configdir}/kwinswitcher.knsrc
%{_kde_configdir}/plasma-overlayrc
%{_kde_configdir}/plasma-themes.knsrc
%{_kde_configdir}/wallpaper.knsrc
%{_kde_configdir}/kfontinst.knsrc
%{_kde_datadir}/dbus-1/services/org.kde.fontinst.service
%{_kde_datadir}/dbus-1/services/org.kde.krunner.service
%{_kde_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_kde_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmclock.service
%{_kde_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%doc %{_kde_docdir}/HTML/en/kcontrol
%doc %{_kde_docdir}/HTML/en/kfontview
%doc %{_kde_docdir}/HTML/en/kmenuedit
%doc %{_kde_docdir}/HTML/en/ksysguard
%doc %{_kde_docdir}/HTML/en/plasma-desktop
%doc %{_kde_docdir}/HTML/en/systemsettings
%{_kde_iconsdir}/Oxygen_*
%{_kde_iconsdir}/KDE_Classic
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/ScreenSavers/kblank.desktop
%{_kde_services}/ScreenSavers/krandom.desktop
%{_kde_services}/ServiceMenus/installfont.desktop
%{_kde_services}/autostart.desktop
%{_kde_services}/bell.desktop
%{_kde_services}/clock.desktop
%{_kde_services}/colors.desktop
%{_kde_services}/cursortheme.desktop
%{_kde_services}/desktop.desktop
%{_kde_services}/desktoppath.desktop
%{_kde_services}/desktoptheme.desktop
%{_kde_services}/deviceinfocategory.desktop
%{_kde_services}/display.desktop
%{_kde_services}/fontinst.desktop
%{_kde_services}/fonts.desktop
%{_kde_services}/fonts.protocol
%{_kde_services}/fontthumbnail.desktop
%{_kde_services}/graphicalinfocategory.desktop
%{_kde_services}/ion-bbcukmet.desktop
%{_kde_services}/ion-debianweather.desktop
%{_kde_services}/ion-envcan.desktop
%{_kde_services}/ion-noaa.desktop
%{_kde_services}/ion-wettercom.desktop
%{_kde_services}/joystick.desktop
%{_kde_services}/kaccess.desktop
%if %{with_drakclock}
%{_kde_services}/kcm_drakclock.desktop
%endif
%{_kde_services}/kcm_keyboard.desktop
%{_kde_services}/kcmaccess.desktop
%{_kde_services}/kcmlaunch.desktop
%{_kde_services}/kcmsmserver.desktop
%{_kde_services}/kded/appmenu.desktop
%{_kde_services}/kded/freespacenotifier.desktop
%{_kde_services}/kded/kephal.desktop
%{_kde_services}/kded/keyboard.desktop
%{_kde_services}/kded/khotkeys.desktop
%{_kde_services}/kded/kwrited.desktop
%{_kde_services}/kded/ktouchpadenabler.desktop
%{_kde_services}/kded/randrmonitor.desktop
%{_kde_services}/kded/statusnotifierwatcher.desktop
%{_kde_services}/keys.desktop
%{_kde_services}/kfontviewpart.desktop
%{_kde_services}/khotkeys.desktop
%{_kde_services}/ksplashthememgr.desktop
%{_kde_services}/kwin
%{_kde_services}/kwin-script-desktopchangeosd.desktop
%{_kde_services}/kwin-script-synchronizeskipswitcher.desktop
%{_kde_services}/kwin-script-videowall.desktop
%{_kde_services}/kwinactions.desktop
%{_kde_services}/kwinadvanced.desktop
%{_kde_services}/kwincompositing.desktop
%{_kde_services}/kwindecoration.desktop
%{_kde_services}/kwinfocus.desktop
%{_kde_services}/kwinmoving.desktop
%{_kde_services}/kwinoptions.desktop
%{_kde_services}/kwinrules.desktop
%{_kde_services}/kwinscreenedges.desktop
%{_kde_services}/kwinscripts.desktop
%{_kde_services}/kwintabbox.desktop
%{_kde_services}/lostfoundcategory.desktop
%{_kde_services}/mouse.desktop
%{_kde_services}/networkinfocategory.desktop
%{_kde_services}/plasma-animator-default.desktop
%{_kde_services}/plasma-applet-activitybar.desktop
%{_kde_services}/plasma-applet-analogclock.desktop
%{_kde_services}/plasma-applet-currentappcontrol.desktop
%{_kde_services}/plasma-applet-devicenotifier.desktop
%{_kde_services}/plasma-applet-digitalclock.desktop
%{_kde_services}/plasma-applet-icon.desktop
%{_kde_services}/plasma-applet-lockout.desktop
%{_kde_services}/plasma-applet-org.kde.notifications.desktop
%{_kde_services}/plasma-applet-panelspacer-internal.desktop
%{_kde_services}/plasma-applet-searchbox.desktop
%{_kde_services}/plasma-applet-sm_hdd_activity.desktop
%{_kde_services}/plasma-applet-sm_ram.desktop
%{_kde_services}/plasma-applet-system-monitor.desktop
%{_kde_services}/plasma-applet-systemtray.desktop
%{_kde_services}/plasma-applet-trash.desktop
%{_kde_services}/plasma-applet-windowlist.desktop
%{_kde_services}/plasma-containment-desktop.desktop
%{_kde_services}/plasma-containment-desktopdashboard.desktop
%{_kde_services}/plasma-containment-netpanel.desktop
%{_kde_services}/plasma-containment-panel.desktop
%{_kde_services}/plasma-containment-sal.desktop
%{_kde_services}/plasma-containment-saverdesktop.desktop
%{_kde_services}/plasma-containmentactions-applauncher.desktop
%{_kde_services}/plasma-containmentactions-contextmenu.desktop
%{_kde_services}/plasma-containmentactions-minimalcontextmenu.desktop
%{_kde_services}/plasma-containmentactions-paste.desktop
%{_kde_services}/plasma-containmentactions-switchactivity.desktop
%{_kde_services}/plasma-containmentactions-switchdesktop.desktop
%{_kde_services}/plasma-containmentactions-switchwindow.desktop
%{_kde_services}/plasma-dataengine-applicationjobs.desktop
%{_kde_services}/plasma-dataengine-apps.desktop
%{_kde_services}/plasma-dataengine-calendar.desktop
%{_kde_services}/plasma-dataengine-devicenotifications.desktop
%{_kde_services}/plasma-dataengine-dict.desktop
%{_kde_services}/plasma-dataengine-executable.desktop
%{_kde_services}/plasma-dataengine-favicons.desktop
%{_kde_services}/plasma-dataengine-filebrowser.desktop
%{_kde_services}/plasma-dataengine-geolocation.desktop
%{_kde_services}/plasma-dataengine-hotplug.desktop
%{_kde_services}/plasma-dataengine-keystate.desktop
%{_kde_services}/plasma-dataengine-mouse.desktop
%{_kde_services}/plasma-dataengine-mpris2.desktop
%{_kde_services}/plasma-dataengine-notifications.desktop
%{_kde_services}/plasma-dataengine-nowplaying.desktop
%{_kde_services}/plasma-dataengine-places.desktop
%{_kde_services}/plasma-dataengine-powermanagement.desktop
%{_kde_services}/plasma-dataengine-rss.desktop
%{_kde_services}/plasma-dataengine-share-addon-im9.desktop
%{_kde_services}/plasma-dataengine-share-addon-imgur.desktop
%{_kde_services}/plasma-dataengine-share-addon-pastebincom.desktop
%{_kde_services}/plasma-dataengine-share-addon-pasteopensuseorg.desktop
%{_kde_services}/plasma-dataengine-share-addon-pasteubuntucom.desktop
%{_kde_services}/plasma-dataengine-share-addon-privatepastecom.desktop
%{_kde_services}/plasma-dataengine-share-addon-simplestimagehosting.desktop
%{_kde_services}/plasma-dataengine-share-addon-wklej.desktop
%{_kde_services}/plasma-dataengine-share-addon-wstaw.desktop
%{_kde_services}/plasma-dataengine-share.desktop
%{_kde_services}/plasma-dataengine-soliddevice.desktop
%{_kde_services}/plasma-dataengine-systemmonitor.desktop
%{_kde_services}/plasma-dataengine-tasks.desktop
%{_kde_services}/plasma-dataengine-time.desktop
%{_kde_services}/plasma-dataengine-weather.desktop
%{_kde_services}/plasma-engine-activities.desktop
%{_kde_services}/plasma-engine-akonadi.desktop
%{_kde_services}/plasma-engine-metadata.desktop
%{_kde_services}/plasma-engine-searchlaunch.desktop
%{_kde_services}/plasma-geolocation-gps.desktop
%{_kde_services}/plasma-geolocation-ip.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-desktop.defaultPanel.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-desktop.findWidgets.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-desktop.photoActivity.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-netbook.defaultPage.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-netbook.defaultPanel.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-netbook.defaultSal.desktop
%{_kde_services}/plasma-packagestructure-dashboard.desktop
%{_kde_services}/plasma-packagestructure-share.desktop
%{_kde_services}/plasma-packagestructure-web.desktop
%{_kde_services}/plasma-pager-default.desktop
%{_kde_services}/plasma-runner-bookmarks.desktop
%{_kde_services}/plasma-runner-calculator.desktop
%{_kde_services}/plasma-runner-kill.desktop
%{_kde_services}/plasma-runner-kill_config.desktop
%{_kde_services}/plasma-runner-locations.desktop
%{_kde_services}/plasma-runner-nepomuksearch.desktop
%{_kde_services}/plasma-runner-plasma-desktop.desktop
%{_kde_services}/plasma-runner-services.desktop
%{_kde_services}/plasma-runner-sessions.desktop
%{_kde_services}/plasma-runner-shell.desktop
%{_kde_services}/plasma-runner-solid.desktop
%{_kde_services}/plasma-runner-webshortcuts.desktop
%{_kde_services}/plasma-runner-windowedwidgets.desktop
%{_kde_services}/plasma-runner-windows.desktop
%{_kde_services}/plasma-sal-bookmarks.desktop
%{_kde_services}/plasma-sal-contacts.desktop
%{_kde_services}/plasma-sal-development.desktop
%{_kde_services}/plasma-sal-education.desktop
%{_kde_services}/plasma-sal-games.desktop
%{_kde_services}/plasma-sal-graphics.desktop
%{_kde_services}/plasma-sal-internet.desktop
%{_kde_services}/plasma-sal-multimedia.desktop
%{_kde_services}/plasma-sal-office.desktop
%{_kde_services}/plasma-sal-system.desktop
%{_kde_services}/plasma-sal-utility.desktop
%{_kde_services}/plasma-scriptengine-applet-dashboard.desktop
%{_kde_services}/plasma-scriptengine-applet-web.desktop
%{_kde_services}/plasma-tasks-default.desktop
%{_kde_services}/plasma-toolbox-desktoptoolbox.desktop
%{_kde_services}/plasma-toolbox-nettoolbox.desktop
%{_kde_services}/plasma-toolbox-paneltoolbox.desktop
%{_kde_services}/plasma-wallpaper-color.desktop
%{_kde_services}/plasma-wallpaper-image.desktop
%{_kde_services}/plasma_applet_keyboard.desktop
%{_kde_services}/plasma_engine_statusnotifieritem.desktop
%{_kde_services}/plasma-applet-org.kde.showActivityManager.desktop
%{_kde_services}/plasma-dataengine-share-addon-imgsusepasteorg.desktop
%{_kde_services}/plasma-dataengine-share-addon-kde.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-desktop.SaL.desktop
%{_kde_services}/plasma-layout-org.kde.plasma-desktop.desktopIcons.desktop
%{_kde_services}/plasma-runner-activityrunner.desktop
%{_kde_services}/powerdevilkeyboardbrightnesscontrolaction.desktop
%{_kde_services}/randr.desktop
%{_kde_services}/recentdocuments.desktop
%{_kde_services}/screensaver.desktop
%{_kde_services}/settings-accessibility.desktop
%{_kde_services}/settings-account-details.desktop
%{_kde_services}/settings-application-and-system-notifications.desktop
%{_kde_services}/settings-application-appearance-and-behavior.desktop
%{_kde_services}/settings-application-appearance.desktop
%{_kde_services}/settings-audio-and-video.desktop
%{_kde_services}/settings-bluetooth.desktop
%{_kde_services}/settings-classic-view.desktop
%{_kde_services}/settings-desktop-appearance.desktop
%{_kde_services}/settings-display.desktop
%{_kde_services}/settings-hardware.desktop
%{_kde_services}/settings-icon-view.desktop
%{_kde_services}/settings-input-devices.desktop
%{_kde_services}/settings-locale.desktop
%{_kde_services}/settings-lost-and-found.desktop
%{_kde_services}/settings-network-and-connectivity.desktop
%{_kde_services}/settings-network-settings.desktop
%{_kde_services}/settings-permissions.desktop
%{_kde_services}/settings-personal-information.desktop
%{_kde_services}/settings-power-management.desktop
%{_kde_services}/settings-removable-devices.desktop
%{_kde_services}/settings-sharing.desktop
%{_kde_services}/settings-shortcuts-and-gestures.desktop
%{_kde_services}/settings-startup-and-shutdown.desktop
%{_kde_services}/settings-system-administration.desktop
%{_kde_services}/settings-window-behaviour.desktop
%{_kde_services}/settings-workspace-appearance-and-behavior.desktop
%{_kde_services}/settings-workspace-behavior.desktop
%{_kde_services}/solid-actions.desktop
%{_kde_services}/standard_actions.desktop
%{_kde_services}/style.desktop
%{_kde_services}/workspaceoptions.desktop
%{_kde_servicetypes}/*.desktop
%{_kde_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_kde_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_kde_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%{_kde_datadir}/sounds/pop.wav
%{_kde_datadir}/wallpapers/*

#------------------------------------------------

%package -n klipper
Summary:	Clipboard manager for KDE
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Conflicts:	%{name} < 2:4.7.97

%description -n klipper
Klipper is a clipboard manager for the KDE interface. 
It allows users of Unix-like operating systems running 
the KDE desktop environment to access a history of X 
Selections, any item of which can be reselected for pasting. 

%files -n klipper
%{_kde_bindir}/klipper
%{_kde_applicationsdir}/klipper.desktop
%doc %{_kde_docdir}/HTML/en/klipper

#------------------------------------------------

%package -n kickoff
Summary:	KDE application launcher
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Conflicts:	%{name} < 2:4.8.97-2

%description -n kickoff
KickOff is the KDE application launcher, or "start menu".

%files -n kickoff
%{_kde_libdir}/libkickoff.so
%{_kde_libdir}/kde4/plasma_applet_launcher.so
%{_kde_libdir}/kde4/plasma_applet_simplelauncher.so
%{_kde_services}/plasma-applet-launcher.desktop
%{_kde_services}/plasma-applet-simplelauncher.desktop

#------------------------------------------------

%package -n plasma-scriptengine-ruby
Summary:	Support for ruby plasma applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	ruby-kde4
Conflicts:	%{name} < 2:4.5.80

%description -n plasma-scriptengine-ruby
This package allow kde4 to use plasma applets written in ruby.

%files -n plasma-scriptengine-ruby
%{_kde_appsdir}/plasma_scriptengine_ruby
%{_kde_services}/plasma-scriptengine-ruby-applet.desktop
%{_kde_services}/plasma-scriptengine-ruby-dataengine.desktop

#------------------------------------------------

%package -n plasma-scriptengine-python
Summary:	Support for ruby python applets
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	python-kde4
Conflicts:	%{name} < 2:4.5.80

%description -n plasma-scriptengine-python
This package allow kde4 to use plasma applets written in python.

%files -n plasma-scriptengine-python
%{py_platsitedir}/PyKDE4/*
%{_kde_appsdir}/plasma_scriptengine_python
%{_kde_services}/plasma-scriptengine-applet-python.desktop
%{_kde_services}/plasma-scriptengine-dataengine-python.desktop
%{_kde_services}/plasma-scriptengine-runner-python.desktop
%{_kde_services}/plasma-scriptengine-wallpaper-python.desktop

#-------------------------------------------------

%define liboxygenstyle_major 4
%define liboxygenstyle %mklibname oxygenstyle %{liboxygenstyle_major}

%package -n %{liboxygenstyle}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{liboxygenstyle}
KDE 4 core library.

%files -n %{liboxygenstyle}
%{_kde_libdir}/liboxygenstyle.so.%{liboxygenstyle_major}*

#------------------------------------------------

%define libweather_ion_major 6
%define libweather_ion %mklibname weather_ion %{libweather_ion_major}

%package -n %{libweather_ion}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libweather_ion}
KDE 4 core library.

%files -n %{libweather_ion}
%{_kde_libdir}/libweather_ion.so.%{libweather_ion_major}*

#------------------------------------------------

%define libkdecorations_major 4
%define libkdecorations %mklibname kdecorations %{libkdecorations_major}

%package -n %{libkdecorations}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkdecorations}
KDE 4 core library.

%files -n %{libkdecorations}
%{_kde_libdir}/libkdecorations.so.%{libkdecorations_major}*

#------------------------------------------------

%define libkscreensaver_major 5
%define libkscreensaver %mklibname kscreensaver %{libkscreensaver_major}

%package -n %{libkscreensaver}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkscreensaver}
KDE 4 core library.

%files -n %{libkscreensaver}
%{_kde_libdir}/libkscreensaver.so.%{libkscreensaver_major}*

#------------------------------------------------

%define libksgrd_major 4
%define libksgrd %mklibname ksgrd %{libksgrd_major}

%package -n %{libksgrd}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libksgrd}
KDE 4 core library.

%files -n %{libksgrd}
%{_kde_libdir}/libksgrd.so.%{libksgrd_major}*

#------------------------------------------------

%define libkwineffects_major 1
%define libkwineffects %mklibname kwineffects %{libkwineffects_major}

%package -n %{libkwineffects}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkwineffects}
KDE 4 core library.

%files -n %{libkwineffects}
%{_kde_libdir}/libkwineffects.so.%{libkwineffects_major}*

#------------------------------------------------------------------------------

%define libkwinglesutils_major 1
%define libkwinglesutils %mklibname kwinglesutils %{libkwinglesutils_major}

%package -n %{libkwinglesutils}
Summary:	Gles2 runtime library for kwin
Group:		System/Libraries

%description -n %{libkwinglesutils}
Kwin GLES2 runtime library.

%files -n %{libkwinglesutils}
%{_kde_libdir}/libkwinglesutils.so.%{libkwinglesutils_major}*

#------------------------------------------------

%define libkworkspace_major 4
%define libkworkspace %mklibname kworkspace %{libkworkspace_major}

%package -n %{libkworkspace}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkworkspace}
KDE 4 core library.

%files -n %{libkworkspace}
%{_kde_libdir}/libkworkspace.so.%{libkworkspace_major}*

#------------------------------------------------

%define libplasmaclock_major 4
%define libplasmaclock %mklibname plasmaclock %{libplasmaclock_major}

%package -n %{libplasmaclock}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libplasmaclock}
KDE 4 core library.

%files -n %{libplasmaclock}
%{_kde_libdir}/libplasmaclock.so.%{libplasmaclock_major}*

#------------------------------------------------

%define libprocesscore_major 4
%define libprocesscore %mklibname processcore %{libprocesscore_major}

%package -n %{libprocesscore}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libprocesscore}
KDE 4 core library.

%files -n %{libprocesscore}
%{_kde_libdir}/libprocesscore.so.%{libprocesscore_major}*

#------------------------------------------------

%define libprocessui_major 4
%define libprocessui %mklibname processui %{libprocessui_major}

%package -n %{libprocessui}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libprocessui}
KDE 4 core library.

%files -n %{libprocessui}
%{_kde_libdir}/libprocessui.so.%{libprocessui_major}*

#------------------------------------------------

%define libkhotkeysprivate_major 4
%define libkhotkeysprivate %mklibname khotkeysprivate %{libkhotkeysprivate_major}

%package -n %{libkhotkeysprivate}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkhotkeysprivate}
KDE 4 core library.

%files -n %{libkhotkeysprivate}
%{_kde_libdir}/libkhotkeysprivate.so.%{libkhotkeysprivate_major}*

#------------------------------------------------

%define libkfontinst_major 4
%define libkfontinst %mklibname kfontinst %{libkfontinst_major}

%package -n %{libkfontinst}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkfontinst}
KDE 4 core library.

%files -n %{libkfontinst}
%{_kde_libdir}/libkfontinst.so.%{libkfontinst_major}*

#------------------------------------------------

%define libkfontinstui_major 4
%define libkfontinstui %mklibname kfontinstui %{libkfontinstui_major}

%package -n %{libkfontinstui}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkfontinstui}
KDE 4 core library.

%files -n %{libkfontinstui}
%{_kde_libdir}/libkfontinstui.so.%{libkfontinstui_major}*

#------------------------------------------------

%define libtaskmanager_major 4
%define libtaskmanager %mklibname taskmanager %{libtaskmanager_major}

%package -n %{libtaskmanager}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libtaskmanager}
KDE 4 core library.

%files -n %{libtaskmanager}
%{_kde_libdir}/libtaskmanager.so.%{libtaskmanager_major}*

#------------------------------------------------

%define liblsofui_major 4
%define liblsofui %mklibname lsofui %{liblsofui_major}

%package -n %{liblsofui}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{liblsofui}
KDE 4 core library.

%files -n %{liblsofui}
%{_kde_libdir}/liblsofui.so.%{liblsofui_major}*

#------------------------------------------------

%define libpowerdevilcore_major 0
%define libpowerdevilcore %mklibname powerdevilcore %{libpowerdevilcore_major}

%package -n %{libpowerdevilcore}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libpowerdevilcore}
KDE 4 core library.

%files -n %{libpowerdevilcore}
%{_kde_libdir}/libpowerdevilcore.so.%{libpowerdevilcore_major}*

#------------------------------------------------

%define libkephal_major 4
%define libkephal %mklibname kephal %{libkephal_major}

%package -n %{libkephal}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkephal}
KDE 4 core library.

%files -n %{libkephal}
%{_kde_libdir}/libkephal.so.%{libkephal_major}*

#------------------------------------------------

%define libksignalplotter_major 4
%define libksignalplotter %mklibname ksignalplotter %{libksignalplotter_major}

%package -n %{libksignalplotter}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libksignalplotter}
KDE 4 core library.

%files -n %{libksignalplotter}
%{_kde_libdir}/libksignalplotter.so.%{libksignalplotter_major}*

#------------------------------------------------

%define libsystemsettingsview_major 2
%define libsystemsettingsview %mklibname systemsettingsview %{libsystemsettingsview_major}

%package -n %{libsystemsettingsview}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libsystemsettingsview}
KDE 4 core library.

%files -n %{libsystemsettingsview}
%{_kde_libdir}/libsystemsettingsview.so.%{libsystemsettingsview_major}*

#------------------------------------------------

%define libplasma_geolocation_interface_major 4
%define libplasma_geolocation_interface %mklibname plasma-geolocation-interface %{libplasma_geolocation_interface_major}

%package -n %{libplasma_geolocation_interface}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libplasma_geolocation_interface}
KDE 4 core library.

%files -n %{libplasma_geolocation_interface}
%{_kde_libdir}/libplasma-geolocation-interface.so.%{libplasma_geolocation_interface_major}*

#------------------------------------------------

%define libplasma_applet_system_monitor_major 4
%define libplasma_applet_system_monitor %mklibname plasma_applet_system_monitor %{libplasma_applet_system_monitor_major}

%package -n %{libplasma_applet_system_monitor}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libplasma_applet_system_monitor}
KDE 4 core library.

%files -n %{libplasma_applet_system_monitor}
%{_kde_libdir}/libplasma_applet-system-monitor.so.%{libplasma_applet_system_monitor_major}*

#-----------------------------------------------------------------------------

%define libplasmagenericshell_major 4
%define libplasmagenericshell %mklibname plasmagenericshell %{libplasmagenericshell_major}

%package -n %{libplasmagenericshell}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libplasmagenericshell}
KDE 4 core library.

%files -n %{libplasmagenericshell}
%{_kde_libdir}/libplasmagenericshell.so.%{libplasmagenericshell_major}*

#-----------------------------------------------------------------------------

%define libkwinglutils_major 1
%define libkwinglutils %mklibname kwinglutils %{libkwinglutils_major}

%package -n %{libkwinglutils}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libkwinglutils}
KDE 4 core library.

%files -n %{libkwinglutils}
%{_kde_libdir}/libkwinglutils.so.%{libkwinglutils_major}*

#-----------------------------------------------------------------------------

%define liboxygenstyleconfig_major 4
%define liboxygenstyleconfig %mklibname oxygenstyleconfig %{liboxygenstyleconfig_major}

%package -n %{liboxygenstyleconfig}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{liboxygenstyleconfig}
KDE 4 core library.

%files -n %{liboxygenstyleconfig}
%{_kde_libdir}/liboxygenstyleconfig.so.%{liboxygenstyleconfig_major}*

#-----------------------------------------------------------------------------

%define powerdevilconfigcommonprivate_major 4
%define libpowerdevilconfigcommonprivate %mklibname powerdevilconfigcommonprivate %{powerdevilconfigcommonprivate_major}

%package -n %{libpowerdevilconfigcommonprivate}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libpowerdevilconfigcommonprivate}
KDE 4 core library.

%files -n %{libpowerdevilconfigcommonprivate}
%{_kde_libdir}/libpowerdevilconfigcommonprivate.so.%{powerdevilconfigcommonprivate_major}*

#-----------------------------------------------------------------------------

%define libpowerdevilui_major 4
%define libpowerdevilui %mklibname powerdevilui %{libpowerdevilui_major}

%package -n %{libpowerdevilui}
Summary:	KDE 4 core library
Group:		System/Libraries

%description -n %{libpowerdevilui}
KDE 4 core library.

%files -n %{libpowerdevilui}
%{_kde_libdir}/libpowerdevilui.so.%{libpowerdevilui_major}*

#-----------------------------------------------------------------------------

%package -n plasma-applet-calendar
Summary:	Plasma applet calendar
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description -n plasma-applet-calendar
Plasma Calendar applet.

%files -n plasma-applet-calendar
%{_kde_libdir}/kde4/plasma_applet_calendar.so
%{_kde_services}/plasma-applet-calendar.desktop

#-----------------------------------------------------------------------------

%package -n plasma-krunner-powerdevil
Summary:	KDE power management applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	upower
Provides:	plasma-krunner
Provides:	powerdevil = %{EVRD}

%description -n plasma-krunner-powerdevil
KDE power management applet.

%files -n plasma-krunner-powerdevil
%{_kde_libdir}/kde4/kded_powerdevil.so
%{_kde_libdir}/kde4/krunner_powerdevil.so
%{_kde_libdir}/kde4/powerdevilbrightnesscontrolaction_config.so
%{_kde_libdir}/kde4/powerdevildimdisplayaction_config.so
%{_kde_libdir}/kde4/powerdevildpmsaction.so
%{_kde_libdir}/kde4/powerdevildpmsaction_config.so
%{_kde_libdir}/kde4/powerdevilrunscriptaction_config.so
%{_kde_libdir}/kde4/powerdevilsuspendsessionaction_config.so
%{_kde_libdir}/kde4/kcm_powerdevilglobalconfig.so
%{_kde_libdir}/kde4/kcm_powerdevilprofilesconfig.so
%{_kde_libdir}/kde4/kcm_powerdevilactivitiesconfig.so
%{_kde_libdir}/kde4/powerdevilhandlebuttoneventsaction_config.so
%{_kde_appsdir}/powerdevil
%{_kde_services}/kded/powerdevil.desktop
%{_kde_services}/powerdevilglobalconfig.desktop
%{_kde_services}/powerdevilhandlebuttoneventsaction.desktop
%{_kde_services}/powerdevilprofilesconfig.desktop
%{_kde_services}/plasma-runner-powerdevil.desktop
%{_kde_services}/powerdevilbrightnesscontrolaction.desktop
%{_kde_services}/powerdevildimdisplayaction.desktop
%{_kde_services}/powerdevildpmsaction.desktop
%{_kde_services}/powerdevilrunscriptaction.desktop
%{_kde_services}/powerdevilsuspendsessionaction.desktop
%{_kde_services}/powerdevilactivitiesconfig.desktop

#-----------------------------------------------------------------------------

%package -n plasma-runner-places
Summary:	Plasma applet places
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-runner

%description -n plasma-runner-places
Plasma runner places.

%files -n plasma-runner-places
%{_kde_libdir}/kde4/krunner_placesrunner.so
%{_kde_services}/plasma-runner-places.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-quicklaunch
Summary:	Launch your favourite Applications
Group:		Graphical desktop/KDE
Requires:	kdebase4-workspace
Provides:	plasma-applet
Obsoletes:	plasma-applet-quicklauncher

%description -n plasma-applet-quicklaunch
Reimplements the quicklaunch applet present in kde3.5.

Features:
- Add icons by specify a .desktop file
- Add icons by dragging .desktop files from other locations
- Rearrange icons by dragging them in place
- Configurable number of rows
- Configurable number of visible icons.

%files -n plasma-applet-quicklaunch
%{_kde_libdir}/kde4/plasma_applet_quicklaunch.so
%{_kde_services}/plasma-applet-quicklaunch.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-battery
Summary:	Simple plasma battery applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	plasma-krunner-powerdevil
Provides:	plasma-applet

%description -n plasma-applet-battery
Simple plasma battery applet.

%files -n plasma-applet-battery
%{_kde_datadir}/kde4/services/plasma-applet-batterymonitor.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-webbrowser
Summary:	A simple webbrowser applet
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description -n plasma-applet-webbrowser
A simple webbrowser applet.

%files -n plasma-applet-webbrowser
%{_kde_libdir}/kde4/plasma_applet_webbrowser.so
%{_kde_services}/plasma-applet-webbrowser.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-system-monitor-temperature
Summary:	A system temperature monitor
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	hddtemp
Requires:	lm_sensors
Provides:	plasma-applet

%description -n plasma-applet-system-monitor-temperature
A system temperature monitor.

%files -n plasma-applet-system-monitor-temperature
%{_kde_libdir}/kde4/plasma_applet_sm_temperature.so
%{_kde_services}/plasma-applet-sm_temperature.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-system-monitor-net
Summary:	A network usage monitor
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	plasma-applet

%description -n plasma-applet-system-monitor-net
A network usage monitor.

%files -n plasma-applet-system-monitor-net
%{_kde_libdir}/kde4/plasma_applet_sm_net.so
%{_kde_services}/plasma-applet-sm_net.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-system-monitor-hwinfo
Summary:	Plasma applet that Show hardware informations
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	lm_sensors
Provides:	plasma-applet

%description -n plasma-applet-system-monitor-hwinfo
Plasma applet that Show hardware informations.

%files -n plasma-applet-system-monitor-hwinfo
%{_kde_libdir}/kde4/plasma_applet_sm_hwinfo.so
%{_kde_services}/plasma-applet-sm_hwinfo.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-system-monitor-hdd
Summary:	A hard disk usage monitor
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	lm_sensors
Provides:	plasma-applet

%description -n plasma-applet-system-monitor-hdd
A hard disk usage monitor.

%files -n plasma-applet-system-monitor-hdd
%{_kde_libdir}/kde4/plasma_applet_sm_hdd.so
%{_kde_datadir}/kde4/services/plasma-applet-sm_hdd.desktop

#-----------------------------------------------------------------------------

%package -n plasma-applet-system-monitor-cpu
Summary:	A CPU usage monitor
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	lm_sensors
Provides:	plasma-applet

%description -n plasma-applet-system-monitor-cpu
A CPU usage monitor.

%files -n plasma-applet-system-monitor-cpu
%{_kde_libdir}/kde4/plasma_applet_sm_cpu.so
%{_kde_services}/plasma-applet-sm_cpu.desktop

#-----------------------------------------------------------------------------

%package -n kdm
Summary:	KDE Desktop Login Manager
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Requires:	kde4-config-file
Provides:	dm
Requires:	kdmfprintplugin

%description -n kdm
KDE Desktop Login Manager.

%post -n kdm
chksession -K
# todo - use native %systemd_post
if [ ! -e /etc/systemd/system/display-manager.service ] ; then
  /bin/systemctl enable kdm.service 2>&1 || :
fi

%preun -n kdm
%systemd_preun kdm.service

%postun -n kdm
chksession -K
%systemd_postun kdm.service

%files -n kdm
%config(noreplace) %{_sysconfdir}/pam.d/kde
%config(noreplace) %{_sysconfdir}/pam.d/kde-np
%config(noreplace) %{_sysconfdir}/logrotate.d/kdm
%{_kde_bindir}/kdm
%{_kde_bindir}/kdmctl
%{_kde_bindir}/genkdmconf
%{_kde_libdir}/kde4/libexec/kdm_config
%{_kde_libdir}/kde4/libexec/kdm_greet
%{_kde_libdir}/kde4/libexec/kfontprint
%{_kde_libdir}/kde4/libexec/krootimage
%attr(4755,root,root) %{_kde_libdir}/kde4/libexec/kcheckpass
%{_kde_libdir}/kde4/kcm_kdm.so
%{_kde_appsdir}/doc/kdm
%dir %{_kde_appsdir}/kdm
%{_kde_appsdir}/kdm/*
%{_kde_datadir}/config/kdm.knsrc
%{_kde_datadir}/config/kdm
%{_kde_services}/kdm.desktop
%{_kde_docdir}/*/*/kdm
%{_kde_libdir}/kde4/kgreet_*
%{_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%{_kde_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkdm.policy
%{_kde_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkdm.service
%{_kde_libdir}/kde4/libexec/kcmkdmhelper
%{_sysconfdir}/dbus-1/system.d/org.kde.powerdevil.backlighthelper.conf
%{_kde_libdir}/kde4/libexec/backlighthelper
%{_kde_datadir}/dbus-1/system-services/org.kde.powerdevil.backlighthelper.service
%{_kde_datadir}/polkit-1/actions/org.kde.powerdevil.backlighthelper.policy
%{_unitdir}/kdm.service
%attr(0775,root,root) %dir %{_localstatedir}/spool/gdm
%attr(0770, root, root) %dir %{_localstatedir}/lib/kdm

#-----------------------------------------------------------------------------

%package -n kinfocenter
Summary:	Kinfocenter
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime
Provides:	kinfocenter4
Requires:	ldetect-lst

%description -n kinfocenter
Kinfocenter is a utility in KDE that provides information
about a computer system.

%files -n kinfocenter
%{_kde_bindir}/kinfocenter
%dir %{_kde_appsdir}/kinfocenter
%{_kde_appsdir}/kinfocenter/*
%{_kde_appsdir}/kcmview1394
%{_kde_libdir}/kde4/kcm_info.so
%{_kde_libdir}/kde4/kcm_opengl.so
%{_kde_libdir}/kde4/kcm_nic.so
%{_kde_libdir}/kde4/kcm_usb.so
%{_kde_libdir}/kde4/kcm_view1394.so
%{_kde_libdir}/kde4/kcm_memory.so
%{_kde_libdir}/kde4/kcm_pci.so
%{_kde_libdir}/kde4/kcm_samba.so
%{_kde_libdir}/kde4/kcm_infosummary.so
%{_kde_libdir}/kde4/devinfo.so
%{_kde_applicationsdir}/kinfocenter.desktop
%{_kde_docdir}/*/*/kinfocenter
%{_kde_services}/dma.desktop
%{_kde_services}/interrupts.desktop
%{_kde_services}/ioports.desktop
%{_kde_services}/kcmusb.desktop
%{_kde_services}/kcmview1394.desktop
%{_kde_services}/nic.desktop
%{_kde_services}/opengl.desktop
%{_kde_services}/scsi.desktop
%{_kde_services}/xserver.desktop
%{_kde_services}/kcm_memory.desktop
%{_kde_services}/kcm_pci.desktop
%{_kde_services}/smbstatus.desktop
%{_kde_services}/devinfo.desktop
%{_kde_services}/kcm_infosummary.desktop

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for kdebase 4
Group:		Development/KDE and Qt
Requires:	kde4-macros
Requires:	kdelibs4-devel
Requires:	%{libkdecorations} = %{EVRD}
Requires:	%{libkscreensaver} = %{EVRD}
Requires:	%{libksgrd} = %{EVRD}
Requires:	%{libkwineffects} = %{EVRD}
Requires:	%{libkwinglesutils} = %{EVRD}
Requires:	%{libkworkspace} = %{EVRD}
Requires:	%{libplasmaclock} = %{EVRD}
Requires:	%{libprocesscore} = %{EVRD}
Requires:	%{libprocessui} = %{EVRD}
Requires:	%{libtaskmanager} = %{EVRD}
Requires:	%{liblsofui} = %{EVRD}
Requires:	%{libkfontinstui} = %{EVRD}
Requires:	%{libkfontinst} = %{EVRD}
Requires:	%{libkhotkeysprivate} = %{EVRD}
Requires:	%{libweather_ion} = %{EVRD}
Requires:	%{libkephal} = %{EVRD}
Requires:	%{libplasma_applet_system_monitor} = %{EVRD}
Requires:	%{libplasma_geolocation_interface} = %{EVRD}
Requires:	%{libplasmagenericshell} = %{EVRD}
Requires:	%{libsystemsettingsview} = %{EVRD}
Requires:	%{libksignalplotter} = %{EVRD}
Requires:	%{libkwinglutils} = %{EVRD}
Requires:	%{liboxygenstyleconfig} = %{EVRD}
Requires:	%{liboxygenstyle} = %{EVRD}
Requires:	%{libpowerdevilcore} = %{EVRD}
Requires:	%{libpowerdevilconfigcommonprivate} = %{EVRD}
Requires:	%{libpowerdevilui} = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on kdebase.

%files devel
%{_kde_libdir}/libpowerdevilui.so
%{_kde_libdir}/libkdecorations.so
%{_kde_libdir}/libkfontinst.so
%{_kde_libdir}/libkfontinstui.so
%{_kde_libdir}/libkscreensaver.so
%{_kde_libdir}/libksgrd.so
%{_kde_libdir}/libkephal.so
%{_kde_libdir}/libkwineffects.so
%{_kde_libdir}/libkworkspace.so
%{_kde_libdir}/libplasma_applet-system-monitor.so
%{_kde_libdir}/libplasmaclock.so
%{_kde_libdir}/libpowerdevilcore.so
%{_kde_libdir}/libprocesscore.so
%{_kde_libdir}/libprocessui.so
%{_kde_libdir}/libtaskmanager.so
%{_kde_libdir}/libweather_ion.so
%{_kde_libdir}/liblsofui.so
%{_kde_libdir}/libplasma-geolocation-interface.so
%{_kde_libdir}/libplasmagenericshell.so
%{_kde_libdir}/libsystemsettingsview.so
%{_kde_libdir}/libksignalplotter.so
%{_kde_libdir}/libkwinglutils.so
%{_kde_libdir}/libkwinglesutils.so
%{_kde_libdir}/liboxygenstyleconfig.so
%{_kde_libdir}/liboxygenstyle.so
%{_kde_libdir}/libpowerdevilconfigcommonprivate.so
%{_kde_includedir}/*
%{_kde_libdir}/kde4/plugins/designer/*
%{_kde_datadir}/apps/cmake/*/*
%{_kde_datadir}/dbus-1/interfaces/*
%{_kde_libdir}/cmake/KDE4Workspace

#-----------------------------------------------------------------------------

%prep
%setup -q -n kde-workspace-%{version}
%patch0 -p1

%if %{with_drakclock}
%patch1 -p1
%patch2 -p1
%endif

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p0
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch18 -p1
%patch19 -p1
%patch26 -p1
%patch27 -p1
%patch50 -p1
%patch100 -p1
%patch101 -p1
%patch104 -p1
%patch106 -p1

%if %{mdvver} == 201210
%patch107 -p1
%endif

rm -fr kdm/kfrontend libs/kdm

tar xf %{SOURCE6}

%build
%cmake_kde4 -DKDE4_XDMCP:BOOL=ON -DKWIN_BUILD_WITH_OPENGLES=ON
%make

%install
%makeinstall_std -C build

%if %{with_drakclock}
install -m 0644 %{SOURCE8} %{buildroot}%{_kde_services}/kcm_drakclock.desktop
%endif

# Remove it because all it does is adding Activities widget to existing panel
rm -f %{buildroot}%{_kde_appsdir}/plasma-desktop/updates/addShowActivitiesManagerPlasmoid.js

rm -fr %{buildroot}%{_kde_appsdir}/kdm/sessions
rm -fr %{buildroot}%{_kde_configdir}/kdm/X*
rm -fr %{buildroot}%{_kde_configdir}/kdm/backgroundrc
rm -fr %{buildroot}%{_kde_configdir}/kdm/kdmrc

install -d -m 0775 %{buildroot}/etc/X11/wmsession.d/
cat << EOF > %{buildroot}/etc/X11/wmsession.d/01KDE
NAME=KDE4
ICON=kde-wmsession.xpm
DESC=The K Desktop Environment
EXEC=%{_kde_bindir}/startkde
SCRIPT:
exec %{_kde_bindir}/startkde
EOF

# Env entry for start kde4
install -d -m 0755 %{buildroot}/etc/profile.d

cat <<EOF > %{buildroot}/etc/profile.d/70kde4.sh
#!/bin/bash

function kde4 {
xinit /etc/X11/Xsession KDE4
}
EOF

# Install kde pam configuration file
install -d -m 0755 %{buildroot}%{_sysconfdir}/pam.d/
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/kde
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/kde-np

%if %{disttag} == "omv"
# OpenMandriva startkde
install -m 0755 %{SOURCE9} %{buildroot}%{_kde_bindir}/startkde
%else
# Rosa startkde
install -m 0755 %{SOURCE9} %{buildroot}%{_kde_bindir}/startkde
%endif

# We need to expand libdir into startkde
sed -e 's,LIBDIR,%{_libdir},g' -i %{buildroot}%{_kde_bindir}/startkde
sed -e 's,KDE4_LIBEXEC_INSTALL_DIR,%{_libdir}/kde4/libexec,g' -i %{buildroot}%{_kde_bindir}/startkde

# systemd implimentation
install -d -m 0775 %{buildroot}%{_unitdir}
# It's different in OMV and ROSA
%if %{disttag} == "omv"
install -m 0644 %{SOURCE11} %{buildroot}%{_unitdir}/kdm.service
%else
install -m 0644 %{SOURCE12} %{buildroot}%{_unitdir}/kdm.service
%endif

# logrotate
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cat << EOF > %{buildroot}%{_sysconfdir}/logrotate.d/kdm
/var/log/kdm.log {
weekly
notifempty
missingok
nocompress
}
EOF

# We use our desktop files. Write over is a better decision than a patch that breaks most of the times
cp -f %{SOURCE4} %{buildroot}%{_kde_applicationsdir}/

# own as part of plymouth/kdm integration hacks (rhbz #551310)
mkdir -p -m775 %{buildroot}%{_localstatedir}/spool/gdm
mkdir -p -m770 %{buildroot}%{_localstatedir}/lib/kdm

sed -i 's!preferences-other!preferences-app-run!g' \
  %{buildroot}%{_kde_services}/settings-startup-and-shutdown.desktop

%check
for f in %{buildroot}%{_kde_applicationsdir}/*.desktop ; do
  desktop-file-validate $f
done

%changelog
* Tue Apr 08 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.8-2
- Add fix-screenlocker-ulock patch from OpenSUSE to fix issues with unlock

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.8-1
- New version 4.11.8

* Thu Mar 20 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.7-3
- Use different kdm.service for ROSA and OpenMandriva

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.7-1
- New version 4.11.7

* Sun Mar 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.6-6
- Use different startkde scripts and Requires for ROSA and OpenMandriva

* Tue Feb 18 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.6-4
- Re-work dbus-wallpaper patch to support more features

* Thu Feb 13 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.6-3
- Update kdm.service to use tty1, no longer require hack for 2012.1 in spec
- Change rosapanel from Requires to Suggests

* Fri Feb 07 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.6-2
- Add dbus-wallpaper patch to make it possible to set wallpaper via dbus

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.6-1
- New version 4.11.6

* Mon Jan 20 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.5-2
- Require udisks2 instead of udisks because kdelibs4 use udisks2 already

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.5-1
- New version 4.11.5

* Wed Dec 18 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-6
- Replace screenlocker-no-fake-focus patch with screenlocker-handle-fake-focus

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.4-1
- New version 4.11.4
- Re-diff screenlocker-background patch

* Mon Nov 25 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-3
- Disable screenlocker-no-fake-focus patch as it seems to be no longer needed

* Wed Nov 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-2
- Add XDG_CURRENT_DESKTOP export to startkde script

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.3-1
- New version 4.11.3
- Drop fix-kcmkdm-config patch because it's merged in upstream
- Update decorations patch

* Thu Oct 10 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-2
- Update startkde script to fix issues with messed up Qt4 style

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.2-1
- New version 4.11.2
- Drop temporary upstream patch200

* Wed Sep 25 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-3
- Backport patch200 from 4.11.2 to fix application icons loading

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-2
- Cooker and Rosa use different tty for X11 so sed it in kdm.service

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.1-1
- New version 4.11.1
- Drop taskbar launchers patch (fixed in upstream)

* Sat Aug 24 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-4
- Add patch to fix plasma crash when there are launchers on taskbar

* Tue Aug 20 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-3
- Add patch to remove activities and launchers from standard panel by default

* Sun Aug 18 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-2
- Add decorations patch to make kde4-windeco-dekorator compile again

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.11.0-1
- New version 4.11.0
- Re-diff menu toptile patch
- Re-diff desktop osd patch
- Re-diff simpleapplet defaults patch
- Re-diff no-hal patch
- Drop no longer needed systemd-shutdown patch
- Add pkgconfig(xcb-keysyms) to BuildRequires
- Drop googlegadgets subpackage as upstream did
- Drop libkwinnvidiahack, libsolidcontrol and libsolidcontrolifaces subpackages
- Update files

* Fri Jul 19 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-2
- Update BuildRequires

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.5-1
- New version 4.10.5

* Thu Jun 20 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-4
- Add udisks to Requires to make sure it's installed

* Thu Jun 20 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-3
- Add patch to use current user's wallpaper for screenlocker if it's a scaled image

* Sat Jun 15 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-2
- Remove addShowActivitiesManagerPlasmoid.js

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.4-1
- New version 4.10.4
- Sort Requires and BuildRequires

* Tue Jun 4 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-12
- Add patch to fix screenlocker greeter focus when screensaver is used

* Thu May 30 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-11
- Update custom startkde script (fix locker part, drop some ancient junk etc)

* Mon May 27 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-10
- Add patch to prefer system locale for KDM when reading it from config fails

* Fri May 24 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-9
- Add patch to fix bug with KCM KDM resetting fonts, style and color (#254430)

* Thu May 23 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-8
- Add patch to fix screenlocker greeter focus after Alt modifier is pressed

* Wed May 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-7
- Add patch to make systemd 194 handle upower stuff in Rosa 2012.1

* Tue May 21 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-6
- Drop Requires pm-utils because it's obsolete
- Use systemd_postun instead of systemd_postun_with_restart for KDM

* Sat May 18 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-4
- Use native preun and postun systemd macros for KDM

* Fri May 17 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-3
- Add patch 7 to fix action labels vertical alignment in Device Notifier applet

* Mon May 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-2
- Turn kdm.service on/off on package install/uninstall in Rosa 2012.1
- Add patch 6 to always show icons in pager widget, even if they don't fit
  window rectangle

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.3-1
- New version 4.10.3

* Thu Apr 25 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-6
- Add workaround for OSD desktop switching issues
- More work on drakclock integration

* Wed Apr 24 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-5
- More work on drakclock integration

* Tue Apr 23 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-3
- Add patch from Mageia to use drakclock for time settings

* Mon Apr 22 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-2
- Add kdm.service file but don't enable this service yet

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2
- Change libsasl-devel to sasl-devel in BuildRequires

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Wed Feb 20 2013 Ural Mullabaev <ural.mullabaev@rosalab.ru> 2:4.10.0-2
- Reverted back KDM greeter plugin header file

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0
- Update files
- Restore googlegadgets subpackage
- Don't use external system tray because it's merged in upstream in 4.10
- Drop merged in upstream l10n-ru patch

* Fri Feb  1 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.9.98-2
- fix empty-%%postun & empty-%%post

* Sun Jan 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.5-1
- New version 4.9.5
- Re-diff l10n-ru patch

* Tue Dec 11 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 2:4.9.4-3
- Fixed KDM password verifying states

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4
- Update fontconfig patch

* Thu Nov 29 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 2:4.9.3-7
- Increased avatars size limits

* Wed Nov 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-6
- Add kde-workspace-4.9.3-fontconfig patch

* Mon Nov 26 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 2:4.9.3-4
- Updated KDM to version 2.7

* Fri Nov 23 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-3
- Add kdebase-workspace-4.9.3-menu-toptile patch to enable kickoff menu top image

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-4
- New version 4.9.2
- Add and use kdebase-workspace-4.9.0-fontconfigdir patch
- Add rpmlint filters

* Fri Sep 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-3
- New Rosa's system tray version 1.1

* Tue Sep 18 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-2
- Drop google gadgets support and subpackage (as it's obsolete)
- Add pkgconfig(xcursor) to BuildRequires

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1
- Replace default system tray with Rosa's one
- Disable l10n-ru patch as we want to push our translations to upstream anyway

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0
- Re-diff l10n-ru patch

* Tue Jul 24 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-2
- Move kickoff to separate package and suggest it

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- Update to 4.8.97
- Add upower to plasma-krunner-powerdevil Requires
- Convert BuildRequires to pkgconfig style
- Make better usage for KDE path macros
- Re-diff and enable startup-sound patch
- Re-diff and enable klippermenu patch
- Re-diff and enable l10n-ru patch

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- Update to 4.8.95

* Tue Jun 26 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.90-1
- Update to 4.8.90
- Disable some patches for now (re-diff is needed)
- Update BuildRequires
- Update file lists
- Spec cleanup

* Fri Jun 08 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.4-1
- update to 4.8.4

* Mon May 21 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-2
- enable gles support

* Thu May 10 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.3-1
- update to 4.8.3

* Tue Apr 24 2012 Ural Mullabaev <ural.mullabaev@rosalab.ru> 4.8.2-4
- Hid trash applet in the Add widgets dialog

* Thu Apr 19 2012 Mikhail Kompaniets <mkompan@mezon.ru> 4.8.2-2
- Russian localization for .desktop files

* Mon Mar 26 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-3
- update kde icons

* Tue Mar 13 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-2
- apply patches really

* Sun Mar 11 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.1-1
- update to 4.8.1

* Tue Mar  6 2012 Arkady L. Shane <arkady.shane@rosalab.ru> 2:4.8.0-2
- another icon in settings-startup-and-shutdown.desktop

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762414
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-2
+ Revision: 758476
- Split klipper in its own package

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758115
- New upstream tarball

* Mon Jan 02 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 748710
- Fix KDM compil
- Fix compil
- Fix compil
- Fix compil
- New version
- Sync kdm with changes of 2011
- Do not versionnate kdm source

* Sun Dec 11 2011 Matthew Dawkins <mattydaw@mandriva.org> 2:4.7.90-1
+ Revision: 740183
- p301 upstreamed
- p300 applied upstream
- fixed BR

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball

  + Dmitry Mikhirev <dmikhirev@mandriva.org>
    - Merged upstream changes to startkde (fixes bug #64566)

* Wed Nov 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-4
+ Revision: 732720
- Add Patch301 to create powerdevikui lib

* Wed Nov 23 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-3
+ Revision: 732698
- Move files to devel
- Use Real upstream commit for P300

* Tue Nov 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-2
+ Revision: 732309
- Fix typo in file list
- Do not install kcontrol test files BKO #287212 )
- New upstream tarball

* Sun Nov 13 2011 Oden Eriksson <oeriksson@mandriva.com> 2:4.7.41-2
+ Revision: 730446
- rebuild

* Thu Sep 08 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.41-1
+ Revision: 698988
- Update Source6: Fix build
- Enhance kdm tarball
- New version 4.7.41
  Handle kdm as a separate source ( Source6 )

* Mon Aug 01 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.40-3
+ Revision: 692709
- Fix file list
- Fix file list
- Fix requires in the devel package
- New version 4.7.40

* Sat Jul 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.90-1
+ Revision: 689389
- Fix file list
- Fix file list
- Fix file list
- New version 4.7 rc1

* Mon Jun 27 2011 Ural Mullabaev <mur@mandriva.org> 2:4.6.4-3
+ Revision: 687463
- Fix kdm patch
- Update kdm patch

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.4-2
+ Revision: 684415
- New version 4.6.4

* Thu May 26 2011 Ural Mullabaev <mur@mandriva.org> 2:4.6.3-2
+ Revision: 679186
- Update kdm patch

* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 2:4.6.3-1
+ Revision: 674399
- new version 4.6.3

* Tue May 03 2011 Alex Burmashev <burmashev@mandriva.org> 2:4.6.2-3
+ Revision: 664582
- kdm theme updte
- kdm theme updte

* Thu Apr 14 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.2-2
+ Revision: 653063
- Fix requires

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.2-1
+ Revision: 650769
- Remove mkrel
- New version 4.6.2
- Fix release
  Add rosapanel as a requires
- Add kdm patch from ROSA

* Thu Mar 10 2011 Funda Wang <fwang@mandriva.org> 2:4.6.1-6
+ Revision: 643239
- rebuild

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.6.0-5
+ Revision: 632975
- New version KDE 4.6 Final

* Fri Jan 07 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.95-5mdv2011.0
+ Revision: 629559
- Fix file list
- New version KDE 4.6 RC2

* Wed Dec 29 2010 Funda Wang <fwang@mandriva.org> 2:4.5.90-5mdv2011.0
+ Revision: 625791
- br network manager

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.90-4mdv2011.0
+ Revision: 624193
- Fix file list
- New upstream tarball

* Sun Dec 19 2010 Funda Wang <fwang@mandriva.org> 2:4.5.85-4mdv2011.0
+ Revision: 622906
- powerdevilcore now versioned

* Sun Dec 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.85-3mdv2011.0
+ Revision: 620602
- Rebuild because of missing rpms
- Fix file list
- Fix file list
- Fix file list
- Do not reload kde4-migrate at each start
  CCBUG: 61898
- Fix file list
- New upstream tarball

* Fri Nov 26 2010 Funda Wang <fwang@mandriva.org> 2:4.5.80-1mdv2011.0
+ Revision: 601487
- update provides
- hal support cannot be disabled
- disable hal support
- should be fixed in other ways
- update description
- New version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 2:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599128
- update file list
- new snapshot 4.5.77
- do not install usb.ids

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1198299.2mdv2011.0
+ Revision: 598769
- default to use usb.ids from ldetect-lst

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 2:4.5.76-0.svn1198299.1mdv2011.0
+ Revision: 598743
- update file list
- new snapshot
- there is no plasma python desktop  now

* Sun Oct 31 2010 John Balcaen <mikala@mandriva.org> 2:4.5.74-0.svn1190490.2mdv2011.0
+ Revision: 590742
- Drop BR for python-kde4 (which is a subpackage of kdebindings.)

* Thu Oct 28 2010 Funda Wang <fwang@mandriva.org> 2:4.5.74-0.svn1190490.1mdv2011.0
+ Revision: 589699
- New snapshot (bybye polkit-kde)

* Tue Oct 19 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1187451.1mdv2011.0
+ Revision: 586753
- correct file list
- new snapshot
- drop merged patches

* Thu Oct 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1185867.1mdv2011.0
+ Revision: 585625
- fix build
- update file list
- new snapshot to fix various bugs

* Sun Oct 10 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1183367.3mdv2011.0
+ Revision: 584593
- add upstream rr1183891 to fix profile loading

* Fri Oct 08 2010 Anssi Hannula <anssi@mandriva.org> 2:4.5.71-0.svn1183367.2mdv2011.0
+ Revision: 584269
- fix file conflict between kdebase4-workspace and kdm

* Thu Oct 07 2010 Funda Wang <fwang@mandriva.org> 2:4.5.71-0.svn1183367.1mdv2011.0
+ Revision: 584089
- fix file list
- update file list
- new snapshot 4.5.71

* Tue Sep 14 2010 Funda Wang <fwang@mandriva.org> 2:4.5.68-1mdv2011.0
+ Revision: 578334
- new snapshot 4.5.68
- patch6 merged upstream (kde#153056)

* Thu Sep 09 2010 Funda Wang <fwang@mandriva.org> 2:4.5.67-2mdv2011.0
+ Revision: 576892
- add missing requries on libpackage

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove old conflicts

* Fri Sep 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.67-1mdv2011.0
+ Revision: 575700
- Fix file list
- Fix BuildRequires
- New version 4.5.67
- Fix groups
- Enable dmtx functionnality in klipper
- Fix file list
- Remove P20
- New version 4.5.65

* Wed Aug 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-3mdv2011.0
+ Revision: 571140
- Rediff and rename Patch0

* Thu Aug 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-2mdv2011.0
+ Revision: 569287
- Disable MALLOC_CHECK
  CCBUG: 60614

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.5.0-1mdv2011.0
+ Revision: 566580
- New upstream tarball
- Update to version 4.5.0

* Wed Jul 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.95-1mdv2011.0
+ Revision: 562462
- Fix file list
- KDE 4.5 RC3
- Update to kde 4.5 RC2

  + John Balcaen <mikala@mandriva.org>
    - Add 2  BuildRequires (qalculate-devel & pciutils-devel)

* Wed Jun 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-20mdv2010.1
+ Revision: 548134
- Update sendmail.desktop translations

* Wed Jun 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-19mdv2010.1
+ Revision: 547322
- Add branch patch fixing crash when moving widget from panel to desktop
- Add branch patch fixing a crash when uninstalling/installing widgets (P117)

* Fri Jun 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-17mdv2010.1
+ Revision: 547068
- Fix Requires in cdialog

* Thu Jun 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-16mdv2010.1
+ Revision: 547025
- Add branch patch fixing kwin crash

* Wed Jun 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-15mdv2010.1
+ Revision: 546958
- Backport a branch patch fixing a plasma netbook crash
- Add in mdv a branch patch for crash in plasma when moving widgets from panel to desktop
  CCBUG: 59576

* Fri May 28 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-14mdv2010.1
+ Revision: 546516
- call kde4-migrate if present
- Do not migrate mails

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-13mdv2010.1
+ Revision: 546140
- Rebuild in release mode
- Fix device notifier default size ( patch from upstream )

* Fri May 21 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-11mdv2010.1
+ Revision: 545557
- Fix to restart X

* Thu May 20 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-10mdv2010.1
+ Revision: 545510
- Simplify wrapper
- Add a fix from rodrido
- Make XKeepCrashing executable
- Remove P312, would need more testing

* Wed May 19 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-9mdv2010.1
+ Revision: 545295
- We deactivate the plymouth integration patch for the moment ( CCBUG: 59334 )
- Fix openvt call

* Mon May 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-8mdv2010.1
+ Revision: 544921
- Add branch patches:
        - append additional x server args after the display name ( P109 )
        - Fix P109 ( P110 )
        - assure it was tokenized correctly ( P111 )
        - Fix crash when adding widgets on the panel ( P112 )
        - Check whether utmp USER_PROCESS entries are still valid  ( P113 )
- Add more translations for sendmail.desktop
- Fix file list
- Only restart X if the user asked to
- Use Wrapper to configure X Server
- Create %%{_localstatedir}/lib/kdm

* Fri May 14 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-6mdv2010.1
+ Revision: 544791
- Final patch for menu tooltips ( Rodrigo you are the best :) )
- As we have tooltips, only show Name on the menu
- Rediff/Enable back drakclock patch
- Add tooltip support in the simpleapplet plasma menu (First version)

* Sun May 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-4mdv2010.1
+ Revision: 544116
- Sync with branch

* Fri May 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-3mdv2010.1
+ Revision: 543097
- Disable Konsole patch as stable release is near

* Thu May 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-2mdv2010.1
+ Revision: 542948
- Fix XFdrake start

* Wed May 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.3-1mdv2010.1
+ Revision: 542506
- Fix plymouth patch
  Add P100: Fix missing icon in plasma-netbook
- Update plymouth patch
  Remove merged patches
- Update to version 4.4.3

* Mon May 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-7mdv2010.1
+ Revision: 541711
- Compile++
- Bump release
- Add other enhancement
- Enhance kdm patch

* Tue Apr 27 2010 Christophe Fergeau <cfergeau@mandriva.com> 2:4.4.2-6mdv2010.1
+ Revision: 539580
- rebuild so that shared libraries are properly stripped again

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Improve lockout patch
      Add patch header

* Sun Apr 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-5mdv2010.1
+ Revision: 538570
- make the debug output prettier

* Thu Apr 15 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-4mdv2010.1
+ Revision: 535094
- Fix file list
- Fix typo
- Add a fedora patch about brightness keys
  backport a plasma netbook trunk fix
- Start the systemsettings modules that requires Root with kdesu
- Add patches to handle better suspend with powerdevil
  Add a Konsole shorcut in the right click from the desktop ( Fedora )
- Add a check on desktop files
- Own %%{_localstatedir}/spool/gdm  ( rhbz #551310 )
- Try to start XFdrake when X does not start OK
- Add french translation
- Add a service file to allow the user to send files by mail
- Add patch to handle transition between plymouth and kdm

* Mon Apr 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-2.1mdv2010.1
+ Revision: 531514
- Fix file list
- Fix trash applet confirmation window
- Rename the freespace notifier
- Remove merged patch

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.2-1mdv2010.1
+ Revision: 530103
- Fix file list
- Remove merged patches
- Update to version 4.4.2
- Fix conf file tagging

* Thu Mar 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-3mdv2010.1
+ Revision: 527353
- Show battery percent left by default

* Fri Mar 12 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-2mdv2010.1
+ Revision: 518347
- This patch reverts change in KDM that made it also grab the mouse, which
  prevents xvkbd from working on tablet PCs.

* Thu Mar 11 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.1-1mdv2010.1
+ Revision: 517979
- Fix gpsd module build
- Sync startkde with the startkde.cmake
- Update startkde to 4.4.1
- Do not silent startkde by default
- Remove merged patches
  Rediff patches
  Add trunk patch to handle screensaver in dragonplayer better
- Update to version 4.4.1

* Mon Feb 22 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-6mdv2010.1
+ Revision: 509623
- Adapt to mandriva-kde4-config
- Fix final layout for the menu, by using RecentlyUsed
- Do not show recent documents this way

* Thu Feb 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-3mdv2010.1
+ Revision: 507725
- Fix default aspect of mdv simpleapplet
- Add security patch
- Fix build for now
- Fix build for now
- Fix logout applet Bug #56389
- Remove kdeglobals locale hack, need to find a proper solution
- Fix defaults var from genkdmconf ( Bug #24510)

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.4.0-1mdv2010.1
+ Revision: 502928
- fix previous patch, i swear it applied before :)
- Remove condition for mdv < 20081
- Translate icons on the taskbar too
- Fix version
- Update to version 4.4.0
- Fix conflicts

* Sun Feb 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-10mdv2010.1
+ Revision: 501531
- Move google-gadget require in the right sub package
- Fix file list removing the %%excludes
- Suggests new googlegadgets package
- Split googleadget in its own subpackage

* Sat Feb 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-7mdv2010.1
+ Revision: 501276
- From opensuse, avoid to increase ~/.xsession-errors too much
- Add opensuse patch about lowdisk notification

* Fri Feb 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-6mdv2010.1
+ Revision: 501130
- Add patch 200: Revert commit 1030993, this add a change in grub that breaks reboot
        because we don't provide grub-set-default
- Add back polit-qt-devel buildrequire
- Build against the good polkit

* Thu Feb 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-4mdv2010.1
+ Revision: 500928
- Bump release
- Better fix for menu translation

* Thu Feb 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-3mdv2010.1
+ Revision: 500916
- Fix menu translations

* Wed Feb 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-2mdv2010.1
+ Revision: 500269
- Fix a crash in kwin
- Do not hardcode mandriva theme, use plasmarc instead

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.98-1mdv2010.1
+ Revision: 499281
- Fix file list
- Fix version
- Use mandriva netbook theme
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.95-1mdv2010.1
+ Revision: 496131
- Update to kde 4.4 Rc2

* Sat Jan 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.90-6mdv2010.1
+ Revision: 495168
- add configchanged icon method
- add filexist method for scripting, will be needed   for the icons widgets
- Do not apply patch24 yet, does not compile
- Do not hardcode netbook to use SingleImage mode
- mark pam files as config files

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 2:4.3.90-3mdv2010.1
+ Revision: 489745
- rebuild for new libxklavier

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix typo
    - Fix file list
    - Fix typo in patch
    - Update to kde 4.4 Rc1
      Rediff patches

* Tue Dec 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-2mdv2010.1
+ Revision: 483202
- Increase release
- Add missing source
- Handle fingerprints in kdm
- Remove redundant buildrequires
- Remove buildrequire in X11-devel

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.85-1mdv2010.1
+ Revision: 480819
- Fix file list
- Update to kde 4.4 BETA 2
  remove merged patches

* Mon Dec 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-3mdv2010.1
+ Revision: 478746
- Fix typo in kdebase-workspace-t1062418-fix-plasma-netbook-start.patch
- P200: Fix plasma netbook start

* Thu Dec 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.80-2mdv2010.1
+ Revision: 473118
- Rebuild because the package is lost on the BS
- Update to kde 4.4 Beta1
  Fix file list

* Sun Nov 29 2009 Funda Wang <fwang@mandriva.org> 2:4.3.77-3mdv2010.1
+ Revision: 471040
- add missing requires

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-2mdv2010.1
+ Revision: 470728
- Add conflicts to ease upgrade

* Fri Nov 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.77-1mdv2010.1
+ Revision: 470680
- Remove merged patch
- Update to kde 4.3.77

* Fri Nov 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-4mdv2010.1
+ Revision: 467611
- Fix krunner freefloating feature

* Wed Nov 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-3mdv2010.1
+ Revision: 467323
- Rebuild for missing package

* Tue Nov 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-2mdv2010.1
+ Revision: 466819
- Fix conflicts

* Mon Nov 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.75-1mdv2010.1
+ Revision: 466580
- Update to kde 4.3.75
  Add sub package :
    - libsystemsettingsview
  Remove sub packages :
    - libnepomukquery  ( moved in kdelibs4 )
    - libnepomukqueryclient
- Obsoletes kde4-style-aurorae

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-5mdv2010.1
+ Revision: 464595
- Rebuild against new qt

* Mon Nov 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-4mdv2010.1
+ Revision: 463535
- Fix top tile patch and enable it again

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-3mdv2010.1
+ Revision: 463099
- Disable custom patches for today

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-2mdv2010.1
+ Revision: 462140
- Remove wrong requires

* Sat Nov 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.73-1mdv2010.1
+ Revision: 462129
- Update to kde 4.3.73
  Rediff patches
  Remove merged patches
  Fix BuildRequires
  Fix file list
- Now kde4-migrate can migrate folders

* Tue Oct 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-10mdv2010.0
+ Revision: 459452
- Remove WIP stuffs
- Backport fixes for panel from trunk to fix reverse plasmoids on panel

* Mon Oct 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-9mdv2010.0
+ Revision: 459362
- Fix typo in kdebase-workspace-4.2.0-fix_gtkrc_iaora.patch

* Sat Oct 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-8mdv2010.0
+ Revision: 459185
- Fix obsoletes
- We are using kde 4.3.2?  so tell it
- Add a migration tool
- Fix typo
- Allow to use right themes with ia ora-kde (patch from lmenut)(Bug #52740)
- Fix krandr obsolete

* Wed Oct 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-7mdv2010.0
+ Revision: 458644
- Fix Kmenu reboot icon

* Mon Oct 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-6mdv2010.0
+ Revision: 458321
- Fix icons in KDM

* Sun Oct 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-5mdv2010.0
+ Revision: 458082
- Obsolete solid-actions-kcm
  Add branched patch to fix double click on systemsettings

* Thu Oct 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-4mdv2010.0
+ Revision: 457553
- Fix typo

* Wed Oct 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.2-3mdv2010.0
+ Revision: 457283
- Sync with branch

* Tue Oct 06 2009 Anne Nicolas <ennael@mandriva.org> 2:4.3.2-2mdv2010.0
+ Revision: 454480
- Add dm as a provide

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.2-1mdv2010.0
+ Revision: 454421
- New upstream release 4.3.2.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove unneeded patch
    - backport patch23 from revision 421699
      add a comment for patch22

  + Thierry Vignaud <tv@mandriva.org>
    - source 1: use pam_namespace for xguest

* Sat Sep 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-11mdv2010.0
+ Revision: 449596
- Add back menu translation patch

* Thu Sep 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-10mdv2010.0
+ Revision: 448115
- Upstream patch to fix a plasma crash

* Wed Sep 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-9mdv2010.0
+ Revision: 447940
- Requires a chksession that allow KDE4

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-8mdv2010.0
+ Revision: 444737
- Fix typo

* Sat Sep 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-7mdv2010.0
+ Revision: 444636
- Remove Language
- Do not use this patch for the moment
- Obsolete kde3 packages
- Remove some unused patches
- More fixes for the device notifier
- Allow adding submenus of the application launcher to the panel
- Obsolete kde3 packages

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added post logout patch through consolekit handling from Fedora.

* Sat Sep 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.1-2mdv2010.0
+ Revision: 438567
- Remove subrel
- Add patch header
  Fix  device notifier size ( from trunk )
- backport patch from trunk

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.1-1mdv2010.0
+ Revision: 423193
- New upstream release 4.3.1.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - polish startkde

* Thu Aug 13 2009 Emmanuel Andry <eandry@mandriva.org> 2:4.3.0-4mdv2010.0
+ Revision: 416101
- add P21 to apply new Air theme in kdm

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix requires

* Fri Aug 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.3.0-3mdv2010.0
+ Revision: 411302
- Fix BuildRequires
- Workaround upstream bug to keep user settings between kde 4.2 and kde           4.3

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.3.0-2mdv2010.0
+ Revision: 409334
- New upstream release 4.3.0.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Handle estonian

* Thu Jul 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.98-1mdv2010.0
+ Revision: 399095
- Set language too
- remove revert unneeded change on libxclavier patch
- Versionnate libxklavier-devel buildrequire

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.96-1mdv2010.0
+ Revision: 394338
- Update to Rc2

* Sat Jul 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-6mdv2010.0
+ Revision: 392205
- Fix patch0
- Need to rediff patch0
- Fix build with libXKlavier
- Backport a taskmanager crash
- Add back kdm patch

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-2mdv2010.0
+ Revision: 389495
- Rebuild for missing packages

* Thu Jun 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.95-1mdv2010.0
+ Revision: 389150
- Update to kde 4.3Rc1

* Sat Jun 20 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.90-2mdv2010.0
+ Revision: 387434
- [Spec 4.3.4.1] Use Descriptions by default on menu

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.90-1mdv2010.0
+ Revision: 382681
- Update to beta2

* Fri May 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.88-1mdv2010.0
+ Revision: 380731
- Update to kde 4.2.88
- Sync mandriva-startkde with upstream startkde

* Sat May 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.87-2mdv2010.0
+ Revision: 378982
- Add libgpsd-devel as BuildRequires
- Fix file list

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.87-1mdv2010.0
+ Revision: 378632
- Update to kde   4.2.87

* Sun May 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-4mdv2010.0
+ Revision: 373981
- Really make drakclock on clock applet usable

* Sun May 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-3mdv2010.0
+ Revision: 373918
- Fix policykit-kde description
- Fix clock patch
  Enable policy-kit support

* Fri May 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.85-2mdv2010.0
+ Revision: 373560
- Rebuild because of missing packages
- Fix drakclock patch
- Update to kde 4.2.85
- Rediff drakclock patch

* Mon May 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371846
- Fix file list
- Update to kde 4.2.71
- Update to kde 4.2.71

* Sat May 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.2mdv2010.0
+ Revision: 370400
- Rebuild for missing package

* Fri May 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 369937
- More build fixes
- Fix version in startkde
  Start to fix build
- Remove more merged patches
- Update to kde 4.2.70
  Remove branch patches
  Rediff patches
  Remove merged trunk patches
  Fix file list
- Fix language selection at first kde start
- Fix conflicts with Gnome keyboard.desktop

* Wed Apr 15 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-18mdv2009.1
+ Revision: 367584
- Another kdebase4 fix for kde3 cohexistency

* Tue Apr 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-17.1mdv2009.1
+ Revision: 367238
- Add back the good context, thanks to all the kde team :)

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-16.1mdv2009.1
+ Revision: 365927
- Add some upstream patches from branch
        - Patch112: Fixing crash in case consolekit is there, but the session is not
        - Patch113: Fix Calendar taking 100%% CPU when resizing KDE bug #187699
        - Patch114: Fix build of Patch113

* Fri Apr 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-15.1mdv2009.1
+ Revision: 365561
- Add branch patches to fix mem leaks
- Add commit log for patch kdebase-workspace-backport-4.3.0-rev943558.patch

* Wed Apr 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-14mdv2009.1
+ Revision: 365241
- Fix powerdevil on multi-user systems.

* Mon Apr 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-12mdv2009.1
+ Revision: 364299
- Backport some patches from the 4.2 branch:
    - Patch107: avoid white flashes when approaching the glowbar
- Add some upstream patches from branch
    - Patch 235: don't call init() on applets when moving them between containments

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-10mdv2009.1
+ Revision: 364107
- Add upstream commit :
    - Patch106: MagicLamp requires OpenGL
- Add some upstream patches from branch
        - Patch101: Fix screensaver size
        - Patch102: krunner: Reset the default palette for the combobox
        - Patch103: Use just kWarning() for X errors, so that users don't report various
        - Patch104: Fix Krunner search
        - Patch105: take care of whitespaces in history as well + fix m_queryRunning

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-8mdv2009.1
+ Revision: 364081
- Fix file list
- Disable krandrtray from autostarting for now (#49503)

* Sat Apr 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-7mdv2009.1
+ Revision: 364058
- Update systemsetting desktop file

* Sat Apr 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-6mdv2009.1
+ Revision: 364028
- Obsolete old kde3 kdm

* Sat Apr 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-5mdv2009.1
+ Revision: 363974
- Add patch234, this patch add back the titles on the menu Recently Used Application , ...
- Add menu titles by default

* Fri Apr 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.2-4mdv2009.1
+ Revision: 363811
- Add back custom mandriva translations to kickoff model

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix regression that prevented to open powerdevil configuration window
    - Add commit logs at the top of the kde svn patches

* Fri Apr 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-2mdv2009.1
+ Revision: 363637
- Fix compilation for simpleapplet.cpp
- Fix menu
- Rediff and add support for complete right click on simple applet
- Apply more patches
- More rediff ( right click ( part 1/2))
- Allow back separators on simple applet
- Add back toptile image
- Port one more patch
- Start to add back simple applet from trunk as our bug is now fixed

* Sun Mar 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.2-1mdv2009.1
+ Revision: 362091
- Fix file list
- Rediff patches
- Add back "Recently Used Applications" feature
  Separator and right click supports will come back later today

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with kde 4.2.2 try#1 packages

* Wed Mar 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-127mdv2009.1
+ Revision: 360981
- Rebuild for missing packages

* Tue Mar 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-126mdv2009.1
+ Revision: 360794
- Try to use standard way for mdv default icon
- Try to use default config for simpleapplet menu button too
- Use mdv icon on kickoff by default too

* Mon Mar 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-124mdv2009.1
+ Revision: 360772
- Fix patch306
- Allow to customize kickoff menu icon

* Mon Mar 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-123mdv2009.1
+ Revision: 360735
- Really apply right click patch
- Apply back Patch19

* Mon Mar 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-121mdv2009.1
+ Revision: 360567
- disable patch19 for the moment

* Sun Mar 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-120mdv2009.1
+ Revision: 360488
- Bump release
- Remove the wrong requires
- Fix patch numbers
- Use mdv icons on the plasmoidviewer
- Fix right click implementation

* Sun Mar 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-17mdv2009.1
+ Revision: 360249
- fix right click patch
- Fix Requires on lm_sensor
- Enable right click on the simple menu applet
- On KDE4 we use krandrrc and not kcmrandrrc anymore

* Wed Mar 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-16mdv2009.1
+ Revision: 357526
- Fix separator patch
- [Trunk] Add support for separators

* Wed Mar 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-15mdv2009.1
+ Revision: 357246
- Obsolete old kde3 packages to ease upgrade
- Bump release

* Wed Mar 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-13.96mdv2009.1
+ Revision: 357023
- Include missing headers
- More obsoletes
- Fix patch16
- Autostart krandrtray
- [BUGFIX] Fix Requires( Bug #48614)
- Suggests plasma-monitor applets
- Rediff and enable back mandriva_menu_toptile patch
- Add an other backport patch
  Fix crash when moving simpleapplet out of the taskbar
- More backports
- Add missing pathes
- Start to backport more trunk fixes for simple applet
  Disable patch16, it will be back when all patches from trunk will be backported

  + Helio Chissini de Castro <helio@mandriva.com>
    - Remember the taskbar group settings for applications

* Mon Mar 09 2009 Arthur Renato Mello <arthur@mandriva.com> 2:4.2.1-10mdv2009.1
+ Revision: 353266
- Use new Mandriva menu button

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add  pm-utils as Requires for solid-powermanagement

* Wed Mar 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-8mdv2009.1
+ Revision: 348663
- [Branch] Allow plasmoids to be placed close to screen edges. (Bug #47508)

* Wed Mar 04 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-7mdv2009.1
+ Revision: 348462
- Fix kdm userlist images
- We don't need add gnome dependency now

* Tue Mar 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-5mdv2009.1
+ Revision: 347769
- [Trunk] Add patch revision  934457 ( Fix crash at startup) ( Bug #48361)

* Tue Mar 03 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-4mdv2009.1
+ Revision: 347741
- KDE 4.2.1 workspace try#2 upstream release

* Tue Mar 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-3mdv2009.1
+ Revision: 347623
- Fix crash at kde startup

* Mon Mar 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.1-2mdv2009.1
+ Revision: 346984
- Fix file list
- fix build
- Fix file list
- Upload new and fixed menu ( recently Used application  is back )
  Please report me quickly any issues
- Remove patch 224 ( Merged in branch revision 923295)
- Fix patch 223
- Remove patch 222 ( backported on branch)
- Remove patch 221 ( backported on branch)
- Remove patch 220 ( backported on branch)
- Remove patches 215 -> 219 ( Merged Upstream)
- Remove patch 214 (Merged upstream)
- Apply patch 213
- Apply patch 212
- Apply patch211
- Rediff patch 210
- Rediff patch 208
- Rediff patch 207
- Remove patch 206 ( fixed in upstream commit 929311)
- Apply patch 205
- Rediff patch 204
- Rediff patch203
- Rediff patch 16
- Rediff patch15
- Add back all the patches removed with an Axe ( i will rediff them one by one)

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.1-1mdv2009.1
+ Revision: 346056
- KDE 4.2.1 try#1 upstream release

* Thu Feb 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-16mdv2009.1
+ Revision: 345020
- [Trunk] Fix crash of quicklaunch applet at start

* Wed Feb 25 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-15mdv2009.1
+ Revision: 344962
- Add Mandriva faces dir to kdm

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix broken patch
    - [Trunk] Add missing save session feature on simpleapplet menu
    - Patch from trunk: Order menu correctly

* Sun Feb 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-12mdv2009.1
+ Revision: 343812
- It is time to add our own translations :)

* Sat Feb 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-11mdv2009.1
+ Revision: 343770
- Add trunk patches to fix menus crashes

* Fri Feb 20 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-10mdv2009.1
+ Revision: 343393
- We need configure clock...

* Tue Feb 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-9mdv2009.1
+ Revision: 341211
- (kephal conf) Use a saner function
- Backport a kdm fix from branch
- Cleaner kephal patch

* Sat Feb 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-7mdv2009.1
+ Revision: 340198
- Add some debug for the menu crash issue

* Sat Feb 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-6mdv2009.1
+ Revision: 340186
- Cleaner Kephal patch
- Backport patch from branch to fix some powerdevil issues ( QMO: 47784 / BKO: 178642)
  Add a draft patch to fix location of kephal config file ( a cleaner one will come just after its review )
- Install ksysguarddrc

* Tue Feb 03 2009 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:4.2.0-5mdv2009.1
+ Revision: 336999
- Make sure gtk colors are not messed up by kde preferences when using Ia Ora
  (#47438)

* Sun Feb 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-4mdv2009.1
+ Revision: 336283
- Add some branch patches for the menu
  Remove patch rev916145 made menu crashy

* Sun Feb 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-3mdv2009.1
+ Revision: 336244
- Add branch patch to fix crash in the menu

* Thu Jan 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.2.0-2mdv2009.1
+ Revision: 335341
- [BUGFIX] Fix  lock-logout applet size ( Bug #47390)

* Tue Jan 27 2009 Helio Chissini de Castro <helio@mandriva.com> 2:4.2.0-1mdv2009.1
+ Revision: 334616
- Clean the < 20090 ifdefs
- Added 4.2.0 upstream try#1 tarball
- removed "always broken" system-settings.desktop patch in favor of using a single file
- Removed already applied SOURCES/kdebase-workspace-backport-4.3.0-rev910752.patch

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add back kdebase-workspace-backport-4.3.0-rev910752.patch ( not completly merged )
      Rediff some patches

* Sun Jan 25 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-14mdv2009.1
+ Revision: 333357
- Bump release
- Backport revisions 914436, 914434 and 914433
- Add a new section in the simple applet to browse easyli the SystemSetting
- Fix export of libkickoff
- Add patches fixing simplemenu applet
- Fix crash in simpleapplet menu upstream revision 914866
- Fix install of libkickoff ( usptream commit 914545 )

* Mon Jan 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-13mdv2009.1
+ Revision: 331233
- Fix build
- Revert commit 331106, the new upstream sentence is better so add it in our catalogs
- Do not show the banner if there is no Recent apps to show
- Use already translated words (should we had the kde one on our catalogs ?)

* Mon Jan 19 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-12mdv2009.1
+ Revision: 331065
- Fix file list
- Fix file list
- Fix backport  911787
- Add Upstream patches  to fix some RecentApps issues
- Add patch header
- Remove unused patches
  Backport menu patch from upstream ( BKO: 177678)
  Rediff mandriva patches ( menu button and toptile)

* Sat Jan 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-9mdv2009.1
+ Revision: 330479
- Some more bluez fixes
- More bluez backports

* Thu Jan 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-8mdv2009.1
+ Revision: 329967
- Backport stuffs for bluez from trunk

  + Helio Chissini de Castro <helio@mandriva.com>
    - Added switch to disable plasma plugins until the egg-chicken issue withj kdebindings are solved

* Tue Jan 13 2009 Arthur Renato Mello <arthur@mandriva.com> 2:4.1.96-7mdv2009.1
+ Revision: 329059
- Add mandriva button to simple apllet menu
- Add mandriva image at simple applet menu top
- Add "run command" to simple applet menu
- Add "recently used" sub menu to simple applet menu

* Mon Jan 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-6mdv2009.1
+ Revision: 328485
- Rebuild because of broken BS

* Sun Jan 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-5mdv2009.1
+ Revision: 328439
- Bump release
- Really fix systemsettings patch
- Add back the systemsetting menu change
- Add Anssi patch for Freetype LCD filtering support

* Sat Jan 10 2009 Anssi Hannula <anssi@mandriva.org> 2:4.1.96-4mdv2009.1
+ Revision: 328112
- fix kdebase4-workspace requiring devel packages

* Sat Jan 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-3mdv2009.1
+ Revision: 328086
- Rebuild against new google-gadget

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.96-2mdv2009.1
+ Revision: 327296
- Fix file list
- Add one more google-gadgets requires
- Fix Requires to not crash when installing a google-gadget (Bug #46590)
- Remove the old xdg patch
  Add upstream xdg menu support

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 2:4.1.85-5mdv2009.1
+ Revision: 319688
- rebuild for new python

* Tue Dec 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-4mdv2009.1
+ Revision: 317749
- Fix file list
- Rebuild in debug mode
- Remove Patch5 uneeded now

* Mon Dec 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-3mdv2009.1
+ Revision: 317399
- Use again mandriva name for SystemSettings
- Do not apply patch5, we do not have mandriva applet for now

* Sun Dec 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-2mdv2009.1
+ Revision: 316952
- Fix menu
- Fix BuildRequires
- Versionnate google-gadgets-devel BuildRequires

* Sat Dec 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.85-1mdv2009.1
+ Revision: 313856
- Fix File list
- Remove merged patch

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.85

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.82-1mdv2009.1
+ Revision: 312897
- Update to kde 4.1.82

* Mon Dec 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.81-3mdv2009.1
+ Revision: 311722
- Add an upstream patch to fix the broken window effects

* Sun Dec 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.81-2mdv2009.1
+ Revision: 311679
- Remove wrong patch
- Disable translation patch for the moment

* Sun Nov 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.81-1mdv2009.1
+ Revision: 308584
- Fix File list
- Update to kde 4.1.81

* Tue Nov 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-6mdv2009.1
+ Revision: 306807
- Split more packages:
   * plasma-applet-system-monitor-net
   * plasma-applet-system-monitor-hwinfo
   * plasma-applet-system-monitor-hdd
   * plasma-applet-system-monitor-cpu
- Add conflicts to ease upgrade
- Slip a little more plasma applets in its own package:
- plasma-applet-sm_temperature
- plasma-applet-webbrowser
- Change quicklaunch summary
- Make plasma-applet-quicklaunch obsoletes plasma-applet-quicklauncher

* Tue Nov 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-5mdv2009.1
+ Revision: 306489
- Remove merged patch
- Obsolete kde4powersave
- Do not apply patch4 for the moment, still a WIP patch
- Remove patch10  Merged upstream

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updated with fresh beta 1 official fixed tarball

* Sat Nov 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-4mdv2009.1
+ Revision: 305819
- Add back webkitkde-devel as BuildRequire

* Sat Nov 22 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-3mdv2009.1
+ Revision: 305771
- Add upstream patch to fix a know regression that break kwin
- Move the battery applet in its own package
- Fix Kephal libs
- Remove webkikde-devel BR as it requires kdebase4-workspace-devel which can not be installed
- Move libkephal out of the devel package

  + Helio Chissini de Castro <helio@mandriva.com>
    - Wrong version requires

* Thu Nov 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.80-1mdv2009.1
+ Revision: 305330
- Fix file list
- Move plasma-applet-quicklaunch in its own package
- Rediff the patches

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-2mdv2009.1
+ Revision: 303424
- Fix FIle list
- Add krunner places in its own package

* Thu Nov 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.73-1mdv2009.1
+ Revision: 302932
- Fix file list
- Update to kde 4.1.73
  Rediff xdg patch
  Remove unneeded patches
- Add a comment
- Remove all powerdevil files from main package
- Split powerdevil in its own package
- move plasma-applet-calendar on its own package
- Add back support for kde defaut menu ( now drakmenustyle can work with kde :) )

  + Funda Wang <fwang@mandriva.org>
    - plasma-calender is moved into workspace main package

* Tue Oct 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.71-5mdv2009.1
+ Revision: 297805
- First try for the plaindesktop
- Add support for google gadgets

* Sat Oct 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.71-3mdv2009.1
+ Revision: 297149
- Say hello back to policyKit support
- Add conflicts

* Fri Oct 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.71-2mdv2009.1
+ Revision: 296999
- Fix BuildRequires
- Fix BuildRequires
- Update to kde 4.1.71

* Tue Oct 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.70-2mdv2009.1
+ Revision: 296167
- Fix Requires on libs for the devel package

* Mon Oct 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.70-1mdv2009.1
+ Revision: 295742
- FIx file list
- Fix BuildRequires
- Fix headers
- Restore old patch
- Update to KDE 4.1.70
  add new libs : lsofui nepomukquery nepomukqueryclient
  Patch not yet applied ConsoleKit, Mandriva Menu
  Remove merged and backport patches
  Fix File List

* Fri Oct 03 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:4.1.2-13mdv2009.0
+ Revision: 291046
- Fix the menu topbar for large menus (#44284)

* Fri Oct 03 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-12mdv2009.0
+ Revision: 290999
- Try to use a elegant form to fix the sound startup
- Fix wrong enconding in the menu - https://qa.mandriva.com/show_bug.cgi?id=44480

* Thu Oct 02 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-11mdv2009.0
+ Revision: 290899
- Fix sizing of menu button. PlasmaSvg is returning a square sizing, not respect original button size.

* Thu Oct 02 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-10mdv2009.0
+ Revision: 290709
- Removed double applet insertion.
- Initial PLasma::Icon modification to fit Mandriva non standard layout buttons. Applet size itself need be better handled.
- Fix double deletion in mandriva menu applet. For some reason this are affected only in x86_64 archs and indirectly was causing
  the crashes related to translation using Utf8. Now system can be used even in greek.

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - Do not write gtkrc files when using IaOra

  + Tiago Salem <salem@mandriva.com.br>
    - fix wrong hal query about suspend method (#44315)

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-9mdv2009.0
+ Revision: 290197
- For some reason, utf translated strings are crashing in x86_64 systems, and a conversion is needed before mennu model is presented in screen. This is a workaround and not the proper fix yet, since the real reason for null pointer was not found.

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-8mdv2009.0
+ Revision: 289943
- Add translation for menu, as use sycoca instead of kservice

* Mon Sep 29 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:4.1.2-6mdv2009.0
+ Revision: 289896
- Make the color configuration module notify all application rootwindows about the changes.
  This makes sure xsettings-kde will be able to apply the newly changed colors to gtk apps.

  + Funda Wang <fwang@mandriva.org>
    - merge translation from kde3 branch

* Sun Sep 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.2-5mdv2009.0
+ Revision: 289078
- Change systemsettings menu entry name
- Fix version in startkde

* Sat Sep 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.2-4mdv2009.0
+ Revision: 288892
- rotate kdm logfiles

* Fri Sep 26 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 2:4.1.2-3mdv2009.0
+ Revision: 288685
- Save the name of the color schemes

* Fri Sep 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.2-2mdv2009.0
+ Revision: 288512
- Allow systemsettings to show on the menu

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.2-1mdv2009.0
+ Revision: 288217
- KDE 4.1.2 arriving.
- Startkde now parses share/kde4/env

* Tue Sep 23 2008 Arthur Renato Mello <arthur@mandriva.com> 2:4.1.1-14mdv2009.0
+ Revision: 287238
- Adding support to use kde4-splash-mdv on startkde script

* Mon Sep 22 2008 Arthur Renato Mello <arthur@mandriva.com> 2:4.1.1-13mdv2009.0
+ Revision: 287149
- Add support for new KDE Splash on startkde script

* Sat Sep 20 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-12mdv2009.0
+ Revision: 286054
- Reintroduce proper systray refactor code

* Sat Sep 20 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-11mdv2009.0
+ Revision: 286050
- Systray not appears due new code and missing dataengine. Code reintroduced in patch.

* Fri Sep 19 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-10mdv2009.0
+ Revision: 286011
- "Soon it will grow, start moving and talking, and then turn into a cat." Well, not anymore :-)
  (c) Spuk 2009

* Fri Sep 19 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-9mdv2009.0
+ Revision: 285975
- Second fix for menu model issues

* Fri Sep 19 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-8mdv2009.0
+ Revision: 285940
- Fix another invalid access that lead menu to crash

* Thu Sep 18 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-7mdv2009.0
+ Revision: 285680
- Switch to mandriva menu instead of simpleapplet
- post branch patch to size of lock applet

* Wed Sep 17 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-6mdv2009.0
+ Revision: 285538
- revert changes of last startkde merge
- Fix menu issue with empty recently used applications

* Tue Sep 16 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-4mdv2009.0
+ Revision: 285187
- Removed invalid patch
- Fix for startkde from upstream package
- MOved wmsession to 01KDE, as requested by fcrozat

* Thu Sep 04 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-3mdv2009.0
+ Revision: 280690
- Convenience requires

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.1-2mdv2009.0
+ Revision: 278187
- Fix conflicts betwenn kdebase4-workspace && kdm

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.1-1mdv2009.0
+ Revision: 277818
- Upgrade test for 4.1.1.

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-20mdv2009.0
+ Revision: 276397
- Fix crash on invalid refcount at mandriva menu

* Tue Aug 26 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-19mdv2009.0
+ Revision: 276077
- kdm face icons now accept png as default
- Initial support for Mandriva menu. Issues in current plasma icon still  prevent proper menu icon

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - exclude battery desktop file too

* Sun Aug 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-17mdv2009.0
+ Revision: 275424
- backport tooltip support

* Sat Aug 23 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-16mdv2009.0
+ Revision: 275257
- Turn off glib loop on kwin to reduce cpu consumption. experimental patch.

* Sun Aug 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-15mdv2009.0
+ Revision: 272991
- Add patch to fix transparency issue

* Wed Aug 13 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-14mdv2009.0
+ Revision: 271415
- Daily branch patch update

* Thu Aug 07 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-13mdv2009.0
+ Revision: 266744
- Raise the release
- Daily branches patch update
- Added plasma notification applet as backport

* Thu Aug 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-11mdv2009.0
+ Revision: 265680
- Update xdg support patch again
- Move krunner_lock on the right package

* Wed Aug 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-9mdv2009.0
+ Revision: 264168
- Second try for the xdg support on the menu

* Tue Aug 05 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-8mdv2009.0
+ Revision: 263968
- Add fixes for simplemenu applet

* Tue Aug 05 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-7mdv2009.0
+ Revision: 263857
- Daily branch patch updates
- Disable plasma battery applet. We're providing kde4powersave and not intend to make our users confuse

* Mon Aug 04 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-6mdv2009.0
+ Revision: 263321
- Say Hello to the Magic Lamp effect

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fixed my patch mess related to branch. Now all patches are in proper order

* Sun Aug 03 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-5mdv2009.0
+ Revision: 262465
- [BUGFIX] Update with branch patches that fix some menus issues (Bug #42308)

* Fri Aug 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-4mdv2009.0
+ Revision: 259220
- Add patch 122 to fix crashes on classic menu applet

* Wed Jul 30 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-3mdv2009.0
+ Revision: 254154
- Start updates from post 4.1.0 branch on cooker only. All patches comes with full description inside.

* Mon Jul 28 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.1.0-2mdv2009.0
+ Revision: 251566
- Update with Release Candidate 1 - 4.1.0

* Sat Jul 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.1.0-1mdv2009.0
+ Revision: 250102
- Update cube effect patch ( lot of bugfixes)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.0

* Thu Jul 17 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.98-7mdv2009.0
+ Revision: 237751
- Update with current consolekit fedora patch as pointed by neoclust and discussed in the bko thread http://bugs.kde.org/show_bug.cgi?id=147790. All patches from Mandriva was integrated alreadyin this fedora patch and we're aiming for a common version

* Mon Jul 14 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.98-6mdv2009.0
+ Revision: 234698
- rc1 tarball ws updated upstream to include systray fix

* Sun Jul 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.98-5mdv2009.0
+ Revision: 234388
- Update cube effcts

* Sun Jul 13 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.0.98-4mdv2009.0
+ Revision: 234308
- Update Cube effects (Now there is a cylinder effects too on it )

* Fri Jul 11 2008 Olivier Blin <blino@mandriva.org> 2:4.0.98-3mdv2009.0
+ Revision: 233829
- rebuild since the BS ate the previous release
- fix autologin for users having a password (by using pam_permit in kde-np pam config)
- move kde pam files to kdm package (used by kdm only, and provided upstream in kdebase-workspace)

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.98-1mdv2009.0
+ Revision: 233204
- Update with Release Candidate 1 - 4.0.98

* Wed Jul 09 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.85-2mdv2009.0
+ Revision: 233151
- Fixed click x double click login issue on kdm list

* Wed Jul 09 2008 Helio Chissini de Castro <helio@mandriva.com> 2:4.0.85-1mdv2009.0
+ Revision: 233107
- First attempt from upstream to fix nasty systray gtk bug. Related to bko https://bugs.kde.org/show_bug.cgi?id=164786

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232325
- Fix File list
- Update to kde 4.0.85
  Remove patches 4,5,6 : Merged upstream

* Sun Jul 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-9mdv2009.0
+ Revision: 232275
- Fix cube effect patch header
- New snapshot of cube effect patch
  Close cube with release of right mouse button. (I do not understand why catching a double click event does not work...)
  FEATURE: 165855

* Sat Jul 05 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-8mdv2009.0
+ Revision: 232019
- New snapshot of cube effect patch
  Now you can move the cube with the mouse

* Wed Jul 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-7mdv2009.0
+ Revision: 230802
- Add patch6 that add missing bluetooth signals ( needed by next kbluetooth4 )

* Wed Jul 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-6mdv2009.0
+ Revision: 230633
- Fix cub effect patch
- Update Cube patch ( now there is a configuration window )

* Tue Jul 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-5mdv2009.0
+ Revision: 230436
- New version of the systray fix patch

* Sun Jun 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-4mdv2009.0
+ Revision: 230023
- Fix cube effect patch
- Update cube effect patch

* Sat Jun 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-3mdv2009.0
+ Revision: 229808
- Update Patch 2 : Cube Effet
  Disable patch 5 for now as it do not work for the moment

* Sat Jun 28 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.84-2mdv2009.0
+ Revision: 229638
- Remove Patch3 : Merged upstream
  Add Experimental patch5, that try to fix the issue with net_applet not visible on the systray

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with new snapshot tarballs 4.0.84

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-2mdv2009.0
+ Revision: 227609
- Strange that last package just missed one of the headers blocking plasmoids to be built

* Fri Jun 20 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-1mdv2009.0
+ Revision: 227487
- Update with new snapshot tarballs 4.0.83

* Wed Jun 18 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-5mdv2009.0
+ Revision: 225366
- Moved cube effect patch to top of patch list.
- Removed all foreign patches that comes from a different codebase.
  Cleaning up help us to find issues as some reported in recent qa article by Frederik
- mdv online desktop removed for now. Planning for a Mandriva Plasmoid in future to replace all this
  features

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add patch11 that add support for cube on the window effects

* Sat Jun 14 2008 Anssi Hannula <anssi@mandriva.org> 1:4.0.82-3mdv2009.0
+ Revision: 219127
- update versioned conflicts for old krandr
- add conflicts to -devel with old kde3 devel packages
- update versioned conflicts in -devel for moved dbus interface files

* Thu Jun 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.82-2mdv2009.0
+ Revision: 218298
- Proper interface dir
- Update with new snapshot tarballs 4.0.82
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.81-3mdv2009.0
+ Revision: 214835
- Fixed consolekit patch
- Update with new snapshot tarballs 4.0.81

* Sun Jun 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.81-2mdv2009.0
+ Revision: 214157
- Fix menu-laucher patch
- Use upstream commit 815052 to associate Alt+F1 by default with the menu

* Fri May 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.81-1mdv2009.0
+ Revision: 213282
- New snapshot 4.0.81
- New snapshot 4.0.81
- Add drakconf with systemsettings on kickoff
- Add patch6 to fix bnc #391765

* Mon May 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-5mdv2009.0
+ Revision: 211402
- Unactivate patch 2 for the moment
- Fix patch 5
- Disable patch5 for the moment
- Explicitly add major
- Obsoletes libplasma1
- Apply patch 5
- Add some functionnalities :
  	- List newly installed apps (upstream commit ) (revision 791871 )
  	- Add the save session feature ( revision 808087 )
  	- Copy suspend parts from ksmserver logout dialog (revision 811622 )
  	- Make drop of local file to Plasma desktop copy to ~/Desktop ( revision 811590 )
  	- Add global shortcut to open start menu ( revision 807732 )

* Sat May 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-2mdv2009.0
+ Revision: 210968
- Fix File List
- [BUGFIX] Make kcheckpass working by making it suid root (Bug #41023)

* Sat May 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 210923
- Versionnate BR
- Own %%_kde_appsdir/ksmserver
- Own %%_kde_appsdir/systemsettings

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 beta1

* Sun May 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-4mdv2009.0
+ Revision: 208820
- Do not build networkmanager support for the moment

* Sun May 18 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-3mdv2009.0
+ Revision: 208687
- Fix conflicts against systemsettings-kde3 (thanks to berthy)

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-2mdv2009.0
+ Revision: 208163
- Versionnate BuildRequire
- Rebuild against new kdepimlibs4

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-1mdv2009.0
+ Revision: 208065
- New version 4.0.74

* Tue May 13 2008 Anssi Hannula <anssi@mandriva.org> 1:4.0.73-2mdv2009.0
+ Revision: 206680
- add Conflicts for old KDE3 packages for smooth upgrade

* Thu May 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-1mdv2009.0
+ Revision: 204571
- Update to kde 4.0.73

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-4mdv2009.0
+ Revision: 203396
- Add back support for mandriva menus

* Tue May 06 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.72-3mdv2009.0
+ Revision: 202213
- Now requires proper config files for kdm
- Removed duplicated and invalid files
- Fixed startkde with current upstream changes
  At this moment, kde 4.1 alpha can start to be used in cooker

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix BuildRequires ( thanks to helio )

* Tue May 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-1mdv2009.0
+ Revision: 201968
- Fix file list (comment for the moment, will be fixed on the next rpm
- Add buildrequire
- Add some BuildRequires
- Update to kde 4.0.72
- Add upstream missing functions (setMaxSourceCount and maxSourceCount)
- add printer-applet files
- New snapshot 4.0.69
- New Snapshot ( 4.0.69 )
  Reverted change from revision 192347 ( made  too much conflicts )
  Remove merged upstream patch ( Patch 100 )

  + Helio Chissini de Castro <helio@mandriva.com>
    - kdm earns their own name now, finally
    - New upstream kde4 4.1 alpha 1
    - Starting to push new infrastructure for devel KDE 4.1. KDE 4 will be on / now. KDE is dead. Long live KDE vi kdenetwork4/SPECS/kdenetwork4.spec ;-)

* Sat Mar 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 191121
- Remvove debug
- remove already included patches
- Update for last stable release 4.0.3

* Tue Mar 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-6mdv2008.1
+ Revision: 186979
- [FEATURE] Add mandriva tools at start on the systray (Bug #38761)

* Mon Mar 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-5mdv2008.1
+ Revision: 183929
- [BUGFIX] Allow to double click on desktop icons (Bug #38597)
- backport patch from 4.0.3 to fix changing wallpapers

* Mon Mar 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-4mdv2008.1
+ Revision: 183472
- Fix install of startkde
- Use external startkde  file
  Use mandriva menu layout (Bug # 38087)

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-3mdv2008.1
+ Revision: 182142
- Rebuild against new qt4 changes

* Sun Mar 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 177701
- Fix File list
- Fix conflict with kde4-kinfocenter (part 1)
- [BUGFIX] Do not crash when the wallpaper do not exist anymore (Bug #37992)
- Add ifdef statement to allow backports again

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream bugfix release 4.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag
    - fix description-line-too-long

* Sun Feb 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-2mdv2008.1
+ Revision: 164815
- Updating for stable KDE 4.0.1
- No more branches. From now, we will be using the monthly official KDE tarballs, as discussed by Mandriva KDE Team

* Fri Jan 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-4.765577.2mdv2008.1
+ Revision: 158079
- Really remove plasma lib to devel package ( thanks thierry )

* Thu Jan 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-4.765577.1mdv2008.1
+ Revision: 157529
- Update for current 4.0 branch

* Wed Jan 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-4mdv2008.1
+ Revision: 157230
- Move devel files out of main package

* Sun Jan 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-3mdv2008.1
+ Revision: 155174
- [FEATURE] Add systemtray patch to allow to have gtk apps on the systray
- [FEATURE] Add ConsoleKit support to kdm (from fedora)

* Sat Jan 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-2mdv2008.1
+ Revision: 155016
- Fix File list so no devel packages are needed anymore

* Thu Jan 10 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 147717
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update for final stable 4.0.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-1.752045.1mdv2008.1
+ Revision: 137370
- New snapshot
  libkwinnvidiahack is now on this package
  Kdm can be started now

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Dec 10 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-1mdv2008.1
+ Revision: 117079
- New snapshot
  Kfontinst, libkfontinst and libkfontinstui are now on workspace

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updating to official 3.97.0

* Sun Dec 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.743949.1mdv2008.1
+ Revision: 114453
- New snapshot

* Fri Nov 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.743105.1mdv2008.1
+ Revision: 114056
- New snapshot

* Wed Nov 28 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.742711.1mdv2008.1
+ Revision: 113774
- New snapshot

* Mon Nov 26 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.741587.4mdv2008.1
+ Revision: 112015
- New snapshot

* Sat Nov 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740034.4mdv2008.1
+ Revision: 111748
- Make file list cleaner
  Add missing plasma file (libkdeinit_plasma.so)

  + Thierry Vignaud <tv@mandriva.org>
    - better description

* Thu Nov 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740034.3mdv2008.1
+ Revision: 111352
- Fix Obsoletes for libkickermain2

* Thu Nov 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740034.2mdv2008.1
+ Revision: 111344
- Fix Obsoletes for libtaskbar{4,5}

* Thu Nov 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740034.1mdv2008.1
+ Revision: 111338
- New snapshot

* Fri Nov 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.0-0.737290.1mdv2008.1
+ Revision: 109044
- KDE 3.96.0

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.2-0.734846.1mdv2008.1
+ Revision: 107511
- New snapshot ( say hello back to nepomuk )

* Fri Nov 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.1-0.731791.1mdv2008.1
+ Revision: 105284
- Fix file list
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.730896.1mdv2008.1
+ Revision: 103768
- Fix file list
- New snapshot

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.729034.1mdv2008.1
+ Revision: 102036
- Fix File List
- New snapshot

* Wed Oct 24 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.728613.2mdv2008.1
+ Revision: 101661
- New snapshot
- New svn snapshot
  Fix File list
  Fix confict against next kdeplayground4-plasma
- Do not package nepomul stuffs, they belong to runtime

* Sun Oct 21 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.727635.2mdv2008.1
+ Revision: 100904
- Clean file list

* Thu Oct 18 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.726385.2mdv2008.1
+ Revision: 100032
- Add conflict as some plasma applets moved from playground to kdebase

* Wed Oct 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.726385.1mdv2008.1
+ Revision: 99742
- Kde 4.0 Beta 3
- New svn snapshot

* Wed Oct 03 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714129.4mdv2008.0
+ Revision: 95202
- Removing external reference to a png file in kde4-wallpaper-mandriva.svg
- Bump release

* Fri Sep 28 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714129.3mdv2008.0
+ Revision: 93600
- Adding patch to disable plasma taskbar
- Adding panel.desktop to autostart kicker
- Adding k4 function to run kde4 apps (Ex: k4 konqueror)
- Bumping release

* Thu Sep 20 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714129.2mdv2008.0
+ Revision: 91567
- Removing mdv2008.0 from Obsoletes tags.
- Making Obsoletes tags versioned

* Sat Sep 15 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.712616.2mdv2008.0
+ Revision: 85841
- Update with revision 712616

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - [BUGFIX] Do not install Kde4 when this is not needed (Bug #31484)

* Thu Sep 06 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.709129.1mdv2008.0
+ Revision: 81147
- Update with revision 709129
- Update with revision 708704

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.708282.1mdv2008.0
+ Revision: 79446
- New package

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.706306.1mdv2008.0
+ Revision: 75070
- Update with revision 706306

* Tue Aug 28 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.705487.2mdv2008.0
+ Revision: 72365
- Update with revision 705487
- Update with revision 704399
- Update with revision 702959
- Update to revision 700912

* Thu Aug 02 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.695685.1mdv2008.0
+ Revision: 58317
- Update for revision 695685
- Update for revision 695647

* Fri Jul 27 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92-0.693361.2mdv2008.0
+ Revision: 56445
- Update to revision 693361
- Disable klipper start for a while
- Using new simplified build
- Update for revision 690341

* Wed Jul 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.689200.2mdv2008.0
+ Revision: 53295
- Better add an svg image than a shell script...

* Wed Jul 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.689200.1mdv2008.0
+ Revision: 53162
- Fix soname now in kdebase
- Update with revision 689200
- Fixed file list
- Fix plasma wallpaper ( hope so )
- Update to revision 688743

* Mon Jul 16 2007 Olivier Blin <blino@mandriva.org> 1:3.91-0.686880.3mdv2008.0
+ Revision: 52444
- require xmessage in the workspace package, it is used in startkde

* Sat Jul 14 2007 Olivier Blin <blino@mandriva.org> 1:3.91-0.686880.2mdv2008.0
+ Revision: 51904
- require xprop and xset in the workspace package, they are used in startkde

* Thu Jul 12 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.686880.1mdv2008.0
+ Revision: 51575
- Fix Mandriva background wallpaper
- Update for revision 686880

* Wed Jul 11 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.91-0.686593.1mdv2008.0
+ Revision: 51431
- Update for match new kdelibs
- Update with revision 683926

* Wed Jul 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682706.1mdv2008.0
+ Revision: 47973
- Fix Conflicts
- New snapshot after monday BIC

* Tue Jul 03 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682449.1mdv2008.0
+ Revision: 47387
- Put them on the right place
- New snapshot

  + Helio Chissini de Castro <helio@mandriva.com>
    - Fix file list
    - Update from svn pos 3.91
    - New svn snapshot with more dolphin fixes
    - Update from svn

* Tue Jun 26 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.680516mdv2008.0
+ Revision: 44518
- Finally a working build of current svn. Kdesktop is about to die.
- Revision 680516
- Update for svn revision 678468

* Tue Jun 19 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.677668mdv2008.0
+ Revision: 41649
- Added nepomuk start/stop scripts on env/shutdown. Is not perfect yet but will help Sebastian to
  demonstrate nepomuk on akademy
- Updated to lates branch. Preview back to work

  + Thierry Vignaud <tv@mandriva.org>
    - fix group

* Mon Jun 18 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.677187mdv2008.0
+ Revision: 41115
- Make dm session works. Previous startkde patch was broken
- Remove dups in file list
- Now we have some background :-)

* Sun Jun 17 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.676742mdv2008.0
+ Revision: 40552
- Added startup by command line. Just need type kde4
- Added env for running kde4 apps. Now just need type kde4env
- Fixed dm entry
- New svn update. Oxygen kwin avaiable

* Sat Jun 16 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.90.2-0.676117mdv2008.0
+ Revision: 40370
- New revision from svn
- New kdebase 4 package

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix File list
    - New svn snapshot

* Wed May 09 2007 Laurent Montel <lmontel@mandriva.org> 1:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25645
- Update release
- new snapshot
- It's possible to compile with enable final

* Wed May 02 2007 Laurent Montel <lmontel@mandriva.org> 1:3.80.3-0.20070502.6mdv2008.0
+ Revision: 20514
- new snapshot
- new snapshot

