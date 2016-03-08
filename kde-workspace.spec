%define with_printer_applet 0
%{?_with_printer_applet: %{expand: %%global with_printer_applet 1}}

%define with_networkmanager 1
%{?_with_networkmanager: %{expand: %%global with_networkmanager 1}}

%define with_drakclock 1
%{?_with_networkmanager: %{expand: %%global with_networkmanager 1}}

%define kdm_version 2.7.2

%bcond_without kscreen

Summary:	KDE 4 application workspace components
Name:		kde-workspace
Version:	4.11.22
Release:	3
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
Source0:	http://download.kde.org/%{ftpdir}/applications/15.08.3/src/kde-workspace-%{version}.tar.xz
Source1:	kde.pam
Source2:	kde-np.pam
Source4:	systemsettings.desktop
Source6:	kdebase-workspace-kdm-%{kdm_version}.tar.bz2
Source8:	kcm_drakclock.desktop
Source9:	omv-startkde
Source10:	rosa-startkde
Source11:	omv-kdm.service
Source12:	rosa-kdm.service
Source13:	kde4-default.desktop
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
# Prefer system locale for KDM when reading it from KDM config fails
Patch10:	kde-workspace-4.10.3-fix-kcmkdm-locale.patch
Patch11:	kdebase-workspace-4.2.0-fix_gtkrc_iaora.patch
# Fix screenlocker greeter focus when screensaver is used
Patch12:	kde-workspace-4.11.4-screenlocker-handle-fake-focus.patch
# Use current wallpaper for screenlocker if it's a scaled image
Patch13:	kde-workspace-4.11.4-screenlocker-background.patch
# Don't add activities and launchers to standard panel by default
Patch14:	kde-workspace-4.11.0-default-panel-layout.patch
# Load session files from /usr/share/xsessions by default
Patch15:	kde-workspace-4.11.11-xsessions.patch
# Adjust session name in kde-plasma.desktop
Patch16:	kde-workspace-4.11.11-desktop-session.patch
Patch18:	kdebase-workspace-4.8.95-startup-sound.patch
Patch19:	kdebase-workspace-4.2.1-use-mdvicon.patch
Patch20:	kde-workspace-4.10.2-BUILD_KCM_RANDR.patch
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
# (tpg) use original patch https://bugs.kde.org/show_bug.cgi?id=206089
# (tpg) updated from Fedora
Patch104:	kde-workspace-4.11.1-kdm_plymouth081.patch
# (tpg) from Fedora - make use of systemd multiseat
Patch105:	kde-workspace-4.11.1-kdm-logind-multiseat.patch
# older Fedora patch, let's keep it for Rosa
Patch106:	kdebase-workspace-4.7.3.fedora-kdm-plymouth.patch
Patch107:	kdebase-workspace-4.11.0-no-hal.patch
Patch108:	kde-workspace-4.11.14-qFuzzyCompare-arm.patch

BuildRequires:	automoc4
BuildRequires:	bdftopcf
BuildRequires:	imake
BuildRequires:	libxml2-utils
BuildRequires:	qt4-qtdbus
BuildRequires:	xrdb
BuildRequires:	boost-devel
BuildRequires:	kdelibs4-devel >= 5:4.14.8
BuildRequires:	kdepimlibs4-devel
BuildRequires:	ieee1284-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	openldap-devel
BuildRequires:	pam-devel
BuildRequires:	python-kde4-devel
BuildRequires:	prison-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(libdmtx)
# google gadgets moved contrib
#BuildRequires:	pkgconfig(libggadget-1.0)
#BuildRequires:	pkgconfig(libggadget-qt-1.0)
BuildRequires:	pkgconfig(libgpsd) >= 3.15
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libpci)
BuildRequires:	pkgconfig(libqalculate)
BuildRequires:	pkgconfig(libraw1394)
# (tpg) needed for patch 107
BuildRequires:	pkgconfig(libsystemd-daemon)
BuildRequires:	pkgconfig(libsystemd-id128)
BuildRequires:	pkgconfig(libsystemd-journal)
BuildRequires:	pkgconfig(libsystemd-login)

BuildRequires:	pkgconfig(libusb)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(lua)
%if %{with_networkmanager}
BuildRequires:	pkgconfig(NetworkManager)
%endif
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(xcb-image)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xcb-renderutil)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xtst)
Requires:	desktop-common-data
Requires:	kde-runtime
Requires:	kde4-integration
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
%if %{with kscreen}
Requires:	kscreen
%else
Requires:	krandr
%endif
%if "%{disttag}" == "omv"
Requires:	homerun
%else
Suggests:	rosapanel
%endif
Conflicts:	kdm < 2:4.10.2-4
Obsoletes:	kdebase4-workspace-googlegadgets < 2:4.11.0
Obsoletes:	%{_lib}solidcontrolifaces4 < 2:4.11.0
Obsoletes:	%{_lib}solidcontrol4 < 2:4.11.0
Obsoletes:	%{_lib}kwinnvidiahack4 < 2:4.11.0
Obsoletes:	kdm < 2:4.11.22-2
Requires(post,preun):	update-alternatives
%rename		kdebase4-workspace

%description
This package contains the KDE 4 application workspace components.

%files
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
%{_kde_libdir}/kde4/kded_statusnotifierwatcher.so
%{_kde_libdir}/kde4/keyboard_layout_widget.so
%{_kde_libdir}/kde4/kfontviewpart.so
%{_kde_libdir}/kde4/kio_fonts.so
%{_kde_libdir}/kde4/krunner_bookmarksrunner.so
%{_kde_libdir}/kde4/krunner_calculatorrunner.so
%{_kde_libdir}/kde4/krunner_kill.so
%{_kde_libdir}/kde4/krunner_locations.so
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
%{_kde_libdir}/kde4/plugins/styles/oxygen.so
%{_kde_libdir}/kde4/powerdevilkeyboardbrightnesscontrolaction_config.so
%{_kde_libdir}/kde4/ion_debianweather.so
%{_kde_libdir}/kde4/krunner_activities.so
%{_kde_libdir}/libkdeinit4_*.so
%{_kde_libdir}/strigi/strigita_font.so
%{_kde_applicationsdir}/kfontview.desktop
%{_kde_applicationsdir}/kmenuedit.desktop
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
%{_datadir}/custom-xsessions/kde4-default.desktop

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop default.desktop %{_datadir}/custom-xsessions/kde4-default.desktop 10
%{_sbindir}/update-alternatives --install %{_kde_autostart}/krunner-alt.desktop krunner.desktop %{_kde_appsdir}/plasma/autostart/krunner.desktop 10
%{_sbindir}/update-alternatives --install %{_kde_autostart}/plasma-desktop-alt.desktop plasma-desktop.desktop %{_kde_appsdir}/plasma/autostart/plasma-desktop.desktop 10

%preun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove default.desktop %{_datadir}/custom-xsessions/kde4-default.desktop
    %{_sbindir}/update-alternatives --remove krunner.desktop %{_kde_appsdir}/plasma/autostart/krunner.desktop
    %{_sbindir}/update-alternatives --remove plasma-desktop.desktop %{_kde_appsdir}/plasma/autostart/plasma-desktop.desktop
fi

#------------------------------------------------

%package -n klipper
Summary:	Clipboard manager for KDE
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Conflicts:	%{name} < 2:4.7.97

%description -n klipper
Klipper is a clipboard manager for the KDE interface. It allows users of
Unix-like operating systems running the KDE desktop environment to access
a history of X Selections, any item of which can be reselected for pasting.

%files -n klipper
%{_kde_bindir}/klipper
%{_kde_applicationsdir}/klipper.desktop
%doc %{_kde_docdir}/HTML/en/klipper

#------------------------------------------------

%package -n kickoff
Summary:	KDE application launcher
Group:		Graphical desktop/KDE
Requires:	kde-runtime
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

%package -n krandr
Summary:	KDE screen management tools
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Conflicts:	%{name} < 2:4.11.10-4

%description -n krandr
KDE screen management tools.

%files -n krandr
%{_kde_bindir}/krandrstartup
%{_kde_bindir}/krandrtray
%{_kde_libdir}/kde4/kcm_randr.so
%{_kde_libdir}/kde4/kded_randrmonitor.so
%{_kde_applicationsdir}/krandrtray.desktop
%{_kde_services}/kded/randrmonitor.desktop
%{_kde_services}/randr.desktop

#------------------------------------------------

%package -n plasma-scriptengine-ruby
Summary:	Support for ruby plasma applets
Group:		Graphical desktop/KDE
Requires:	kde-runtime
Conflicts:	%{name} < 2:4.5.80

%description -n plasma-scriptengine-ruby
This package allow kde4 to use plasma applets written in ruby.

%files -n plasma-scriptengine-ruby
%{_kde_appsdir}/plasma_scriptengine_ruby
%{_kde_services}/plasma-scriptengine-ruby-applet.desktop
%{_kde_services}/plasma-scriptengine-ruby-dataengine.desktop

#------------------------------------------------

%package -n plasma-scriptengine-python
Summary:	Support for python plasma applets
Group:		Graphical desktop/KDE
Requires:	kde-runtime
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
Requires:	kde-runtime
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
Requires:	kde-runtime
Requires:	upower
Provides:	plasma-krunner

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
Requires:	kde-workspace
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
Requires:	kde-workspace
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
Requires:	kde-runtime
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
Requires:	kde-runtime
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
Requires:	kde-runtime
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
Requires:	kde-runtime
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
Requires:	kde-runtime
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
Requires:	kde-runtime
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
Requires:	kde-runtime
Requires:	lm_sensors
Provides:	plasma-applet

%description -n plasma-applet-system-monitor-cpu
A CPU usage monitor.

%files -n plasma-applet-system-monitor-cpu
%{_kde_libdir}/kde4/plasma_applet_sm_cpu.so
%{_kde_services}/plasma-applet-sm_cpu.desktop

#-----------------------------------------------------------------------------

%package -n kde4-integration
Summary:	KDE4 integration plugin
Group:		Graphical desktop/KDE
Conflicts:	kde-workspace < 2:4.11.20

%description -n kde4-integration
This plugin provides integration of pure Qt4 applications with KDE4 Workspace.

%files -n kde4-integration
%{_kde_libdir}/kde4/plugins/gui_platform/libkde.so

#-----------------------------------------------------------------------------

%package -n kinfocenter
Summary:	Kinfocenter
Group:		Graphical desktop/KDE
Requires:	kde-runtime
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
Requires:	kdelibs-devel
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
%rename		kdebase4-workspace-devel

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

rm -fr kdm/kfrontend libs/kdm
tar xf %{SOURCE6}

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
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch26 -p1
%patch27 -p1
%patch50 -p1
%patch100 -p1
%patch101 -p1

%if "%{disttag}" == "omv"
# OpenMandriva Plymouth and KDM patches
%patch104 -p1
%patch105 -p1
%else
# ROSA Plymouth and KDM patches
%patch106 -p1
%endif

%patch107 -p1
%patch108 -p1

%build
%cmake_kde4 -Wno-dev \
	-DBUILD_KCM_RANDR:BOOL=ON \
	-DKDE4_XDMCP:BOOL=ON \
	-DKWIN_BUILD_WITH_OPENGLES=ON \
	-DBUILD_kdm:BOOL=OFF
	
%make

%install
%makeinstall_std -C build

%if %{with_drakclock}
install -m 0644 %{SOURCE8} %{buildroot}%{_kde_services}/kcm_drakclock.desktop
%endif

# Remove it because all it does is adding Activities widget to existing panel
rm -f %{buildroot}%{_kde_appsdir}/plasma-desktop/updates/addShowActivitiesManagerPlasmoid.js

install -d -m 0755 %{buildroot}%{_datadir}/xsessions/
install -d -m 0755 %{buildroot}%{_datadir}/custom-xsessions/
install -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/custom-xsessions/kde4-default.desktop

rm -fr %{buildroot}%{_kde_appsdir}/kdm/sessions
rm -fr %{buildroot}%{_kde_configdir}/kdm/X*
rm -fr %{buildroot}%{_kde_configdir}/kdm/backgroundrc
rm -fr %{buildroot}%{_kde_configdir}/kdm/kdmrc

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

%if "%{disttag}" == "omv"
# OpenMandriva startkde
install -m 0755 %{SOURCE9} %{buildroot}%{_kde_bindir}/startkde
%else
# Rosa startkde
install -m 0755 %{SOURCE9} %{buildroot}%{_kde_bindir}/startkde
%endif

# We need to expand libdir into startkde
sed -e 's,LIBDIR,%{_libdir},g' -i %{buildroot}%{_kde_bindir}/startkde
sed -e 's,KDE4_LIBEXEC_INSTALL_DIR,%{_libdir}/kde4/libexec,g' -i %{buildroot}%{_kde_bindir}/startkde

# We use our desktop files. Write over is a better decision than a patch that breaks most of the times
cp -f %{SOURCE4} %{buildroot}%{_kde_applicationsdir}/

# own as part of plymouth/kdm integration hacks (rhbz #551310)
mkdir -p -m775 %{buildroot}%{_localstatedir}/spool/gdm
mkdir -p -m770 %{buildroot}%{_localstatedir}/lib/kdm

sed -i 's!preferences-other!preferences-app-run!g' \
  %{buildroot}%{_kde_services}/settings-startup-and-shutdown.desktop

# Provide these files via alternatives to avoid file conflicts with BE::Shell
mkdir -p %{buildroot}%{_kde_appsdir}/plasma/autostart
mv %{buildroot}%{_kde_autostart}/krunner.desktop %{buildroot}%{_kde_appsdir}/plasma/autostart/
mv %{buildroot}%{_kde_autostart}/plasma-desktop.desktop %{buildroot}%{_kde_appsdir}/plasma/autostart/

%check
for f in %{buildroot}%{_kde_applicationsdir}/*.desktop ; do
  desktop-file-validate $f
done
