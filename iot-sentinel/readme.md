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

| Identifier        | Device                                                Model | WiFi    | ZigBee  | Ethernet | Z-Wave  | Other   |
|-------------------|-------------------------------------------------------------|---------|---------|----------|---------|---------|
| Aria              | Fitbit Aria WiFi-enabled scale                              | :check: | -       | -        | -       | -       |
| HomeMaticPlug     | Homematic pluggable switch HMIP-PS                          | -       | -       | -        | -       | :check: |
| Withings          | Withings Wireless Scale WS-30                               | :check: | -       | -        | -       | -       |
| MAXGateway        | MAX! Cube LAN Gateway for MAX! Home automation sensors      | -       | -       | :check:  | -       | :check: |
| HueBridge         | Philips Hue Bridge model 3241312018                         | -       | :check: | :check:  | -       | -       |
| HueSwitch         | Philips Hue Light Switch PTM 215Z                           | -       | :check: | -        | -       | -       |
| EdnetGateway      | Ednet.living Starter kit power Gateway                      | :check: | -       | -        | -       | :check: |
| EdnetCam          | Ednet Wireless indoor IP camera Cube                        | :check: | -       | :check:  | -       | -       |
| EdimaxCam         | Edimax IC-3115W Smart HD WiFi Network Camera                | :check: | -       | :check:  | -       | -       |
| Lightify          | Osram Lightify Gateway                                      | :check: | :check: | -        | -       | -       |
| WeMoInsightSwitch | WeMo Insight Switch model F7C029de                          | :check: | -       | -        | -       | -       |
| WeMoLink          | WeMo Link Lighting Bridge model F7C031vf                    | :check: | :check: | -        | -       | -       |
| WeMoSwitch        | WeMo Switch model F7C027de                                  | :check: | -       | -        | -       | -       |
| D-LinkHomeHub     | D-Link Connected Home Hub DCH-G020                          | :check: | -       | :check:  | :check: | -       |
| D-LinkDoorSensor  | D-Link Door & Window sensor                                 | -       | -       | -        | :check: | -       |
| D-LinkDayCam      | D-Link WiFi Day Camera DCS-930L                             | :check: | -       | :check:  | -       | -       |
| D-LinkCam         | D-Link HD IP Camera DCH-935L                                | :check: | -       | -        | -       | -       |
| D-LinkSwitch      | D-Link Smart plug DSP-W215                                  | :check: | -       | -        | -       | -       |
| D-LinkWaterSensor | D-Link Water sensor DCH-S160                                | :check: | -       | -        | -       | -       |
| D-LinkSiren       | D-Link Siren DCH-S220                                       | :check: | -       | -        | -       | -       |
| D-LinkSensor      | D-Link WiFi Motion sensor DCH-S150                          | :check: | -       | -        | -       | -       |
| TP-LinkPlugHS110  | TP-Link WiFi Smart plug HS110                               | :check: | -       | -        | -       | -       |
| TP-LinkPlugHS100  | TP-Link WiFi Smart plug HS100                               | :check: | -       | -        | -       | -       |
| EdimaxPlug1101W   | Edimax SP-1101W Smart Plug Switch                           | :check: | -       | -        | -       | -       |
| EdimaxPlug2101W   | Edimax SP-2101W Smart Plug Switch                           | :check: | -       | -        | -       | -       |
| SmarterCoffee     | Smarter SmarterCoffee coffee machine SMC10-EU               | :check: | -       | -        | -       | -       |
| iKettle2          | Smarter iKettle 2.0 water kettle SMK20-EU                   | :check: | -       | -        | -       | -       |

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
