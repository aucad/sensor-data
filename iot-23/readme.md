# Stratophere Lboratory’s Aposemat IoT-23

**Description**

A labeled dataset with malicious and benign IoT network traffic.

IoT-23 is a new dataset of network traffic from Internet of Things (IoT)
devices. It has 20 malware captures executed in IoT devices, and 3 captures for
benign IoT devices traffic. It was first published in January 2020, with
captures ranging from 2018 to 2019. This IoT network traffic was captured in the
Stratosphere Laboratory, AIC group, FEL, CTU University, Czech Republic. Its
goal is to offer a large dataset of real and labeled IoT malware infections and
IoT benign traffic for researchers to develop machine learning algorithms. This
dataset and its research is funded by Avast Software, Prague.

**Data files & Format**

| Name                     | Details         | Benign | Malicious |     |   Total |       Split |
|:-------------------------|:----------------|:------:|:---------:|-----|--------:|------------:|
| CTU-Honeypot-Capture-4-1 | Philips HUE     |  452   |     0     |     |     452 |     100 / 0 |
| CTU-Honeypot-Capture-5-1 | Amazon Echo     |  1374  |     0     |     |    1374 |     100 / 0 |
| CTU-Honeypot-Capture-7-1 | Somfy Door Lock |  130   |     0     |     |     130 |     100 / 0 |
| CTU-Malware-Capture-8-1  | Hakai           |  2181  |   8222    |     |   10403 |     20 / 80 |
| CTU-Malware-Capture-20-1 | Torii           |  3193  |    16     |     |    3209 |   99.5 / .5 |
| CTU-Malware-Capture-21-1 | Torii           |  3272  |    14     |     |    3286 |   99.5 / .5 |
| CTU-Malware-Capture-34-1 | Mirai           |  1923  |   21222   |     |   23145 |      8 / 92 |
| CTU-Malware-Capture-42-1 | Trojan          |  4420  |     6     |     |    4426 |   99.8 / .2 |
| CTU-Malware-Capture-44-1 | Mirai           |  211   |    26     |     |     237 |     90 / 10 |
| CTU-Malware-Capture-1-1  | Hide and Seek   | 469275 |  539473   |     | 1008748 | 46.5 / 53.5 |

These files have been preprocessed: changed to CSV format, and missing values (`-`) have been
replaced with null values.

**Attribute descriptions**

| Attribute         | Type     | Description                                                                 |
|:------------------|:---------|:----------------------------------------------------------------------------|
| `ts`              | `int`    | Timestamp of the capture                                                    |
| `uid`             | `str`    | ID of the capture                                                           |
| `id_orig.h`       | `str`    | Originating IP where the attack happened                                    |
| `id_orig.p`       | `int`    | Port used by the responder                                                  |
| `id_resp.h`       | `str`    | IP address of the device on which capture happened.                         |
| `id_resp.p`       | `int`    | Port used from the response from the device on which the capture happened.  |
| `proto`           | `str`    | Network protocol                                                            |
| `service`         | `str`    | Application protocol                                                        |
| `duration`        | `float`  | Duration of the transmission between device and attacker.                   |
| `orig_bytes`      | `int`    | Amount of data sent to the device                                           |
| `resp_bytes`      | `int`    | Amount of data sent by the device                                           |
| `conn_state`      | `str`    | State of the connection                                                     |
| `local_orig`      | `bool`   | the connection originated locally                                           |
| `local_resp`      | `bool`   | Whether the response originated locally                                     |
| `missed_bytes`    | `int`    | Amount of missed bytes in a message                                         |
| `history`         | `str`    | History of the state of the connection                                      |
| `orig_pkts`       | `int`    | Amount of packets sent to the device                                        |
| `orig_ip_bytes`   | `int`    | Amount of bytes sent to the device                                          |
| `resp_pkts`       | `int`    | Amount of packets sent from the device                                      |
| `resp_ip_bytes`   | `int`    | Amount of bytes sent from the device                                        |
| `tunnel_parents`  | `str`    | ID of connection if tunneled                                                |
| `label`           | `str`    | Type of capture, benign or malicious                                        |
| `detailed-label`  | `str`    | Type of the malicious capture                                               |

**Label descriptions**

| Label   | Description                                                                                                                                             |
|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attack  | An attack that cannot be identified.                                                                                                                    |
| Benign  | Traffic that is not suspicious.                                                                                                                         |
| C&C     | “Command and Control” type attacks take control of the device to perform various episodes in the future.                                                |
| FD      | The C&C server sends a file to the infected device                                                                                                      |
| HB      | This label indicates that packets sent on this connection track the infected host by the C&C server.                                                    |
| HB-A    | The C&C server checks the status of the infected device while the verification method remains unidentified.                                             |
| HB-FD   | The C&C server checks the status of the infected device by sending small files.                                                                         |
| Mirai   | Connections have characteristics of a Mirai botnet. This label is added when the flows have similar patterns as the most commonly known Mirai attacks.  |
| HPS     | Information is gathered from a device for a future attack.                                                                                              |
| Torii   | The Torii botnet performs the attack.                                                                                                                   |
| DDoS    | The infected device is performing a DDoS attack.                                                                                                        |
| Okiru   | The Okiru botnet performs the attack.                                                                                                                   |

FD = File Download, HB=Heart Beat, A=Attack, HPS=HorizontalPortScan, DDS=denial
of a service attack

More details and explanation of data and
labels: <https://www.stratosphereips.org/datasets-iot23/>

**Dataset source**

<https://www.stratosphereips.org/datasets-iot23/>

**Terms of Use**

If you are using this dataset for your research, please reference it as
“Sebastian Garcia, Agustin Parmisano, & Maria Jose Erquiaga. (2020). IoT-23: A
labeled dataset with malicious and benign IoT network traffic (Version 1.0.0)
[Data set]. Zenodo. http://doi.org/10.5281/zenodo.4743746”

