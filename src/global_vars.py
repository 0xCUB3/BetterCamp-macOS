import os


# Global Variables
macModel = os.popen("sysctl hw.model").read().split(":")[1].strip()
selected_iso = ""
selected_usb = ""

# Links to Bootcamp Drivers
pre_2011 = "http://swcdn.apple.com/content/downloads/57/55/041-84868-A_402D0DFI39/6uz8hhgtd4b87t00mrq0uihiop5ivumsbk/BootCampESD.pkg"
_2011_2012 = "http://swcdn.apple.com/content/downloads/57/55/041-84868-A_402D0DFI39/6uz8hhgtd4b87t00mrq0uihiop5ivumsbk/BootCampESD.pkg"
post_2012 = "http://swcdn.apple.com/content/downloads/24/21/041-88430-A_MH044N1M88/l1tfz2ccakcy7ko79ugzcw0naadra581o3/BootCampESD.pkg"
