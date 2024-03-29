# 3D PAWS

3D PAWS is a Python3 library used to run the various sensors of a [3D-PAWS station](https://sites.google.com/ucar.edu/3dpaws/home). This library supports the following sensors: BMP280, BME280, HTU21d, MCP9808, AS5600, 55300-00-02-A, and SS451A. Note that you need to install this software on a raspberry pi in order for it to work.

## Installation
We recommend using our OS image on your raspberry pi. In order to do that, download the [OS image](https://drive.google.com/file/d/1cMh5CbSSyAjFs-N96DbZOGF94u9en5ae/view?usp=share_link) and load the zipped file onto your pi using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/). 

In order to update to the latest software version, all you need to do is open a command terminal (make sure you're in /home/pi, which is the default when opening a terminal) and type

```bash
sudo python3 update_3d_paws.py
```

Once that's done, move on to Set Variables. If you want to update manually, continue to Manual Installation. 

### Manual Installation
You'll need to download and unpack the software by using the following commands in order. If 3d-paws is already installed on your system, refer to the Update section instead.

```bash
cd /home/pi/
sudo apt-get install git
sudo git clone https://github.com/3d-paws/3d_paws
cd 3d_paws/
sudo python3 setup.py install
```

Once the 3D PAWS library is successfully installed, run the following command:
```bash
sudo python3 environment.py
```
Note: this will delete anything already in the cron (this is to ensure no issues occur when updating the 3D-PAWS software). If the pi is only used for 3d-paws (which is recommended) then this won't be an issue. 

## Set Variables
The software will run without any changes made during this step. However, we recommend at least changing pressure level and altitude to ensure the data is accurate. You'll also want to activate CHORDS so the data is is sent to the database. There are two ways of doing this.

Recommended Way: Launch the GUI (it has a shortcut on the desktop). In the GUI, there is a Settings button in the top left, containing 3 options. Click through each of them, changing any variables you need to. Descriptions for these variables are noted in the GUI.  

Other Way: Update the variables.txt file directly, which is on located your Desktop (/home/pi/Desktop). It is formatted as follows: recording_interval,chords_interval,chords_on/off,station_id,chords_site,pressure_level,test_mode,altitude. 

## Usage
### Remote Viewing
If you need to remote into the pi, there are multiple ways to do so.

1. SSH (requires pi's ip address)
```bash
username: pi
password: Wrf2Pi8!
```

2. AnyDesk (requires pi's AnyDesk id)
```bash
password: 3d_paws!
```

3. Teamviewer (requires pi's Teamviewer id)
```bash
password: ps2222
```

### Launching the Software
You can either launch the GUI from the desktop by double clicking the icon, or from the terminal.
```bash
sudo python3 /home/pi/3d_paws/scripts/gui/main.py
```
### Finding the Data
If the option is activated, the pi will report to CHORDS and/or backup data to the RAL server. If you want to locate your data locally, you can find it in /home/pi/data/. Data gathered over a 24-hour period are stored into a single file.

## Update
The software will update itself every Monday morning at midnight UTC. To force an update sooner, open a terminal (make sure you're in /home/pi, which is the default when opening a terminal) and type 

```bash
sudo python3 update_3d_paws.py
```

## Help
For any questions or problems you might have, please email both Paul Kucera (pkucera@ucar.edu) and Joey Rener (jrener@ucar.edu).

## License
[MIT](https://choosealicense.com/licenses/mit/)