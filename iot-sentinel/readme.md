# Aalto University IoT SENTINEL: IoT Devices Captures

This dataset was used for experiments regarding IoT device-type identification.

This dataset represents the traffic emitted during the setup of 31 smart home
IoT devices of 27 different types (4 types are represented by 2 devices each).
Each setup was repeated at least 20 times per device-type. Each directory
contains several pcap files, each representing a setup of the given device
directory. Files are named Setup-X-Y-STA.pcap where X is the person realizing
the setup and Y is the sequence number of the given capture. The file
_iotdevice-mac.txt contains the MAC address of the considered IoT device.

### Devices

| #   | Identifier        | Device Model                                           | WiFi | ZigBee | Ethernet | Z-Wave | Other |
|-----|:------------------|:-------------------------------------------------------|------|--------|----------|--------|-------|
| 1   | Aria              | Fitbit Aria WiFi-enabled scale                         | ✔    | -      | -        | -      | -     |
| 2   | HomeMaticPlug     | Homematic pluggable switch HMIP-PS                     | -    | -      | -        | -      | ✔     |
| 3   | Withings          | Withings Wireless Scale WS-30                          | ✔    | -      | -        | -      | -     |
| 4   | MAXGateway        | MAX! Cube LAN Gateway for MAX! Home automation sensors | -    | -      | ✔        | -      | ✔     |
| 5   | HueBridge         | Philips Hue Bridge model 3241312018                    | -    | ✔      | ✔        | -      | -     |
| 6   | HueSwitch         | Philips Hue Light Switch PTM 215Z                      | -    | ✔      | -        | -      | -     |
| 7   | EdnetGateway      | Ednet.living Starter kit power Gateway                 | ✔    | -      | -        | -      | ✔     |
| 8   | EdnetCam          | Ednet Wireless indoor IP camera Cube                   | ✔    | -      | ✔        | -      | -     |
| 9   | EdimaxCam         | Edimax IC-3115W Smart HD WiFi Network Camera           | ✔    | -      | ✔        | -      | -     |
| 10  | Lightify          | Osram Lightify Gateway                                 | ✔    | ✔      | -        | -      | -     |
| 11  | WeMoInsightSwitch | WeMo Insight Switch model F7C029de                     | ✔    | -      | -        | -      | -     |
| 12  | WeMoLink          | WeMo Link Lighting Bridge model F7C031vf               | ✔    | ✔      | -        | -      | -     |
| 13  | WeMoSwitch        | WeMo Switch model F7C027de                             | ✔    | -      | -        | -      | -     |
| 14  | D-LinkHomeHub     | D-Link Connected Home Hub DCH-G020                     | ✔    | -      | ✔        | ✔      | -     |
| 15  | D-LinkDoorSensor  | D-Link Door & Window sensor                            | -    | -      | -        | ✔      | -     |
| 16  | D-LinkDayCam      | D-Link WiFi Day Camera DCS-930L                        | ✔    | -      | ✔        | -      | -     |
| 17  | D-LinkCam         | D-Link HD IP Camera DCH-935L                           | ✔    | -      | -        | -      | -     |
| 18  | D-LinkSwitch      | D-Link Smart plug DSP-W215                             | ✔    | -      | -        | -      | -     |
| 19  | D-LinkWaterSensor | D-Link Water sensor DCH-S160                           | ✔    | -      | -        | -      | -     |
| 20  | D-LinkSiren       | D-Link Siren DCH-S220                                  | ✔    | -      | -        | -      | -     |
| 21  | D-LinkSensor      | D-Link WiFi Motion sensor DCH-S150                     | ✔    | -      | -        | -      | -     |
| 22  | TP-LinkPlugHS110  | TP-Link WiFi Smart plug HS110                          | ✔    | -      | -        | -      | -     |
| 23  | TP-LinkPlugHS100  | TP-Link WiFi Smart plug HS100                          | ✔    | -      | -        | -      | -     |
| 24  | EdimaxPlug1101W   | Edimax SP-1101W Smart Plug Switch                      | ✔    | -      | -        | -      | -     |
| 25  | EdimaxPlug2101W   | Edimax SP-2101W Smart Plug Switch                      | ✔    | -      | -        | -      | -     |
| 26  | SmarterCoffee     | Smarter SmarterCoffee coffee machine SMC10-EU          | ✔    | -      | -        | -      | -     |
| 27  | iKettle2          | Smarter iKettle 2.0 water kettle SMK20-EU              | ✔    | -      | -        | -      | -     |

### Dataset source

<https://research.aalto.fi/en/datasets/iot-devices-captures>

### Terms of Use

Please refer to the following publication when citing this dataset:

Markus Miettinen, Samuel Marchal, Ibbad Hafeez, N. Asokan, Ahmad-Reza Sadeghi,
Sasu Tarkoma, “IoT Sentinel: Automated Device-Type Identification for Security
Enforcement in IoT,” in Proc. 37th IEEE International Conference on Distributed
Computing Systems (ICDCS 2017), Jun. 2017.

<https://arxiv.org/abs/1611.04880>
