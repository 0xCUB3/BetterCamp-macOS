import os


# Global Variables
macModel = os.popen("sysctl hw.model").read().split(":")[1].strip()
selected_iso = ""
selected_usb = ""

# Links to Bootcamp Drivers
bc_pre_2011 = "http://swcdn.apple.com/content/downloads/57/55/041-84868-A_402D0DFI39/6uz8hhgtd4b87t00mrq0uihiop5ivumsbk/BootCampESD.pkg"
bc_2011_2012 = "http://swcdn.apple.com/content/downloads/57/55/041-84868-A_402D0DFI39/6uz8hhgtd4b87t00mrq0uihiop5ivumsbk/BootCampESD.pkg"
bc_post_2012 = "http://swcdn.apple.com/content/downloads/24/21/041-88430-A_MH044N1M88/l1tfz2ccakcy7ko79ugzcw0naadra581o3/BootCampESD.pkg"

# Mac Models
pre_2011 = [
    'MacBook5,1',
    'MacBook5,2',
    'MacBook6,1',
    'MacBook7,1',
    'MacBookAir1,1',
    'MacBookAir2,1',
    'MacBookAir3,1',
    'MacBookAir3,2',
    'MacBookPro4,1',
    'MacBookPro4,2',
    'MacBookPro4,3',
    'MacBookPro5,1',
    'MacBookPro5,2',
    'MacBookPro5,3',
    'MacBookPro5,4',
    'MacBookPro5,5',
    'MacBookPro5,6',
    'MacBookPro6,1',
    'MacBookPro6,2',
    'MacBookPro7,1',
    'MacPro3,1',
    'MacPro4,1',
    'MacPro5,1'
    'iMac8,1',
    'iMac9,1',
    'iMac10,1',
    'iMac11,1',
    'iMac11,2',
    'iMac11,3',
    'MacMini3,1',
    'MacMini4,1',
    'Xserve2,1',
    'Xserve3,1'
]

_2011_2012 = [
    'MacBookAir4,1',
    'MacBookAir4,2',
    'MacBookAir5,1',
    'MacBookAir5,2',
    'MacBookAir6,1',
    'MacBookPro8,1',
    'MacBookPro8,2',
    'MacBookPro8,3',
    'MacBookPro9,1',
    'MacBookPro9,2',
    'MacBookPro10,1',
    'MacBookPro10,2',
    'iMac12,1',
    'iMac12,2',
    'iMac13,1',
    'iMac13,2',
    'iMac13,3',
    'MacMini5,1',
    'MacMini5,2',
    'MacMini5,3',
    'MacMini6,1',
    'MacMini6,2',
]

_2013_2020 = [
    'MacBook8,1',
    'MacBook8,2',
    'MacBook9,1',
    'MacBook10,1',
    'MacBookAir6,1',
    'MacBookAir6,2',
    'MacBookAir7,1',
    'MacBookAir7,2',
    'MacBookAir8,1',
    'MacBookAir8,2',
    'MacBookAir9,1'
    'MacBookPro11,1',
    'MacBookPro11,2',
    'MacBookPro11,3',
    'MacBookPro11,4',
    'MacBookPro11,5',
    'MacBookPro13,1',
    'MacBookPro13,2',
    'MacBookPro13,3',
    'MacBookPro14,1',
    'MacBookPro14,2',
    'MacBookPro14,3',
    'MacBookPro15,1',
    'MacBookPro15,2',
    'MacBookPro15,3',
    'MacBookPro15,4',
    'MacBookPro16,1',
    'MacBookPro16,2',
    'MacBookPro16,3',
    'MacBookPro16,4',
    'iMac14,1',
    'iMac14,2',
    'iMac14,3',
    'iMac14,4',
    'iMac15,1',
    'iMac15,2',
    'iMac16,1',
    'iMac16,2',
    'iMac17,1',
    'iMac18,1',
    'iMac18,2',
    'iMac18,3',
    'iMac19,1',
    'iMac19,2',
    'iMac20,1',
    'iMac20,2',
    'MacMini7,1',
    'MacMini8,1',
    'MacPro6,1',
    'MacPro7,1',
    'iMacPro1,1',
]