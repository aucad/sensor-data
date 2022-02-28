# Aalto Univeristy IoT SENTINEL: IoT devices captures

**Description**

This dataset represents the traffic emitted during the setup of 31 smart home
IoT devices of 27 different types (4 types are represented by 2 devices each).
Each setup was repeated at least 20 times per device-type. Each directory
contains several pcap files, each representing a setup of the given device
directory. Files are named Setup-X-Y-STA.pcap where X is the person realizing
the setup and Y is the sequence number of the given capture. The file
_iotdevice-mac.txt contains the MAC address of the considered IoT device.

**Devices**

| Identifier        | Device                                                Model | WiFi               | ZigBee             | Ethernet           | Z-Wave             | Other              |
|-------------------|-------------------------------------------------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| Aria              | Fitbit Aria WiFi-enabled scale                              | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| HomeMaticPlug     | Homematic pluggable switch HMIP-PS                          | -                  | -                  | -                  | -                  | :heavy_check_mark: |
| Withings          | Withings Wireless Scale WS-30                               | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| MAXGateway        | MAX! Cube LAN Gateway for MAX! Home automation sensors      | -                  | -                  | :heavy_check_mark: | -                  | :heavy_check_mark: |
| HueBridge         | Philips Hue Bridge model 3241312018                         | -                  | :heavy_check_mark: | :heavy_check_mark: | -                  | -                  |
| HueSwitch         | Philips Hue Light Switch PTM 215Z                           | -                  | :heavy_check_mark: | -                  | -                  | -                  |
| EdnetGateway      | Ednet.living Starter kit power Gateway                      | :heavy_check_mark: | -                  | -                  | -                  | :heavy_check_mark: |
| EdnetCam          | Ednet Wireless indoor IP camera Cube                        | :heavy_check_mark: | -                  | :heavy_check_mark: | -                  | -                  |
| EdimaxCam         | Edimax IC-3115W Smart HD WiFi Network Camera                | :heavy_check_mark: | -                  | :heavy_check_mark: | -                  | -                  |
| Lightify          | Osram Lightify Gateway                                      | :heavy_check_mark: | :heavy_check_mark: | -                  | -                  | -                  |
| WeMoInsightSwitch | WeMo Insight Switch model F7C029de                          | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| WeMoLink          | WeMo Link Lighting Bridge model F7C031vf                    | :heavy_check_mark: | :heavy_check_mark: | -                  | -                  | -                  |
| WeMoSwitch        | WeMo Switch model F7C027de                                  | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| D-LinkHomeHub     | D-Link Connected Home Hub DCH-G020                          | :heavy_check_mark: | -                  | :heavy_check_mark: | :heavy_check_mark: | -                  |
| D-LinkDoorSensor  | D-Link Door & Window sensor                                 | -                  | -                  | -                  | :heavy_check_mark: | -                  |
| D-LinkDayCam      | D-Link WiFi Day Camera DCS-930L                             | :heavy_check_mark: | -                  | :heavy_check_mark: | -                  | -                  |
| D-LinkCam         | D-Link HD IP Camera DCH-935L                                | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| D-LinkSwitch      | D-Link Smart plug DSP-W215                                  | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| D-LinkWaterSensor | D-Link Water sensor DCH-S160                                | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| D-LinkSiren       | D-Link Siren DCH-S220                                       | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| D-LinkSensor      | D-Link WiFi Motion sensor DCH-S150                          | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| TP-LinkPlugHS110  | TP-Link WiFi Smart plug HS110                               | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| TP-LinkPlugHS100  | TP-Link WiFi Smart plug HS100                               | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| EdimaxPlug1101W   | Edimax SP-1101W Smart Plug Switch                           | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| EdimaxPlug2101W   | Edimax SP-2101W Smart Plug Switch                           | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| SmarterCoffee     | Smarter SmarterCoffee coffee machine SMC10-EU               | :heavy_check_mark: | -                  | -                  | -                  | -                  |
| iKettle2          | Smarter iKettle 2.0 water kettle SMK20-EU                   | :heavy_check_mark: | -                  | -                  | -                  | -                  |

<!-- **Data files & Format** -->

**Dataset source**

<https://research.aalto.fi/en/datasets/iot-devices-captures>

**Terms of Use**

Please refer to the following publication when citing this dataset:

Markus Miettinen, Samuel Marchal, Ibbad Hafeez, N. Asokan, Ahmad-Reza Sadeghi,
Sasu Tarkoma, “IoT Sentinel: Automated Device-Type Identification for Security
Enforcement in IoT,” in Proc. 37th IEEE International Conference on Distributed
Computing Systems (ICDCS 2017), Jun. 2017.

<https://arxiv.org/abs/1611.04880>
