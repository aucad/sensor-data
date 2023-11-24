# Sensor Datasets

Summary and description of datasets in this repository.

|   #   | Dataset                                                                     | Description                        | Files |    Rows | 
|:-----:|:----------------------------------------------------------------------------|:-----------------------------------|:-----:|--------:|
| **1** | **[MavLab Dataset](mavlab)**                                                | **Indoor sensor is on/off**        |   2   |         |
|       | — [March](mavlab/2003_march.csv)                                            | March 2003 readings                |       |    1192 |
|       | — [April](mavlab/2003_april.csv)                                            | April 2003 readings                |       |    3015 | 
|       |                                                                             |                                    |       |         |
| **2** | **[Activity Recognition (MIT)](ar-mit)**                                    | **Single-resident apartment data** |   6   |         |
|       | Subject 1                                                                   | Apartment 1                        |       |         |
|       | — [activity data](ar-mit/1_activities_data.csv)                             | Activity readings                  |       |    1475 |
|       | — [activities](ar-mit/1_activities.csv)                                     | List of activities                 |       |      33 |
|       | — [sensors](ar-mit/1_sensors.csv)                                           | List of sensors                    |       |      76 |
|       | Subject 2                                                                   | Apartment 2                        |       |         |
|       | — [activity data](ar-mit/2_activities_data.csv)                             | Activity readings                  |       |    1040 |
|       | — [activities](ar-mit/2_activities.csv)                                     | List of activities                 |       |      35 |
|       | — [sensors](ar-mit/2_sensors.csv)                                           | List of sensors                    |       |      70 |
|       |                                                                             |                                    |       |         |
| **3** | **[Activity Recognition (U. of Amsterdam)](ar-ams)**                        | **Single-resident apartment data** |   2   |         |
|       | — [activities](ar-ams/activities.csv)                                       | List of activities                 |       |     246 |
|       | — [sensors](ar-ams/sensors.csv)                                             | Sensor data                        |       |    1320 |
|       |                                                                             |                                    |       |         |
| **4** | **[AMPds](ampds)**                                                          | **Utility meter readings**         |  33   |         |
|       | — [Electricity B1E](ampds/Electricity_B1E-1.csv)                            | Bedroom electricity                |       | 1051200 |
|       | — [NaturalGas FRG](ampds/NaturalGas_FRG-1.csv)                              | Furnace Gas                        |       | 1051200 |
|       | — [Water WHW](ampds/Water_WHW-1.csv)                                        | Whole-House Water                  |       | 1051200 |
|       |                                                                             |                                    |       |         |
| **5** | **[Aposemat IoT-23](iot-23)**                                               | **Network data (WireShark)**       |   9   |         |
|       | — [CTU-Honeypot-Capture-4-1](iot-23/CTU-Honeypot-Capture-4-1-labeled.csv)   | benign flows (24h)                 |       |     452 |
|       | — [CTU-Honeypot-Capture-5-1](iot-23/CTU-Honeypot-Capture-5-1-labeled.csv)   | benign flows (5.4h)                |       |    1374 |
|       | — [CTU-Honeypot-Capture-7-1](iot-23/CTU-Honeypot-Capture-7-1-labeled.csv)   | benign flows (1.4h)                |       |     130 |
|       | — [CTU Malware Capture 1-1](iot-23/12-attr/CTU-IoT-Malware-Capture-1-1.csv) | malicious flows (112h)             |       | 1005507 |
|       | — [CTU Malware Capture 8-1](iot-23/CTU-Malware-Capture-8-1-labeled.csv)     | malicious flows (24h)              |       |   10403 |
|       | — [CTU Malware Capture 20-1](iot-23/CTU-Malware-Capture-20-1-labeled.csv)   | malicious flows (24h)              |       |    3209 |
|       | — [CTU Malware Capture 21-1](iot-23/CTU-Malware-Capture-21-1-labeled.csv)   | malicious flows (24h)              |       |    3286 |
|       | — [CTU Malware Capture 34-1](iot-23/CTU-Malware-Capture-34-1-labeled.csv)   | malicious flows (24h)              |       |   23145 |
|       | — [CTU Malware Capture 42-1](iot-23/CTU-Malware-Capture-42-1-labeled.csv)   | malicious flows (8h)               |       |    4426 |
|       | — [CTU Malware Capture 44-1](iot-23/CTU-Malware-Capture-44-1-labeled.csv)   | malicious flows (2h)               |       |     237 |
|       |                                                                             |                                    |       |         |                                                                           |                                    |       |         |
| **6** | **[IoT SENTINEL (Aalto)](iot-sentinel)**                                    | **IoT device type prediction**     |  540  |         |
|       |                                                                             |                                    |       |         |
| **7** | **[Mid-Atlantic CCDC](maccdc)**                                             | **Capture files (pcap)**           |   1   |         |
|       | — [maccdc2012_00016](maccdc/maccdc2012_00016.csv)                           |                                    |       |   20000 |
|       |                                                                             |                                    |       |         |
| **8** | **[UNSW-NB15](unsw-nb15)**                                                  | **Network capture with attacks**   |   2   |         |
|       | — [UNSW-NB15_1](unsw-nb15/unsw-nb15_1_sampled.csv)                          |                                    |       |    7000 |
|       | — [UNSW-NB15_Training 10K](unsw-nb15/unsw-nb15_training_10K.csv)            |                                    |       |   10000 |

**Notes:**

- Some of these datasets are from here: <http://casas.wsu.edu/datasets/>
- Network pcap files: <https://www.netresec.com/index.ashx?page=PcapFiles/>
- Very large datasets (> 50 MB) are not included here => download from source

**Potential Dataset**

| Dataset           | Network     | Year | Attack Categories                                       |
|:------------------|:------------|:----:|:--------------------------------------------------------|
| [CICIDS2017][DS5] | Traditional | 2017 | DoS, DDoS, SSH-Patator, Web, PortScan, FTP-Patator, Bot |
| [CICIDS2018][DS6] | Traditional | 2018 | Bruteforce Web, DoS, DDoS, Botnet, Infilteration        |
| [CTU-13][DS2]     | Traditional | 2011 | Botnet                                                  |
| [Kyoto][DS3]      | Traditional | 2015 | Botnet                                                  |
| [NSL-KDD][DS1]    | Traditional | 2009 | DoS, Probe, User 2 Root and Remote to User              |

[DS1]: https://www.unb.ca/cic/datasets/nsl.html
[DS2]: https://www.stratosphereips.org/datasets-ctu13
[DS3]: http://www.takakura.com/Kyoto_data/
[DS5]: https://www.kaggle.com/datasets/cicdataset/cicids2017
[DS6]: https://www.unb.ca/cic/datasets/ids-2018.html

