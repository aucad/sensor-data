# Stratosphere Laboratory’s Aposemat IoT-23

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

| Name                     | Details         | Benign | Malicious |   Split    |
|:-------------------------|:----------------|:------:|:---------:|:----------:|
| CTU Honeypot Capture 4-1 | Philips HUE     |  452   |     0     |  100 / 0   |
| CTU Honeypot Capture 5-1 | Amazon Echo     |  1374  |     0     |  100 / 0   |
| CTU Honeypot Capture 7-1 | Somfy Door Lock |  130   |     0     |  100 / 0   |
| CTU Malware Capture 8-1  | Hakai           |  2181  |   8222    |  20 / 80   |
| CTU Malware Capture 20-1 | Torii           |  3193  |    16     | 99.5 / 0.5 |
| CTU-Malware-Capture-21-1 | Torii           |  3272  |    14     | 99.5 / 0.5 |
| CTU-Malware-Capture-34-1 | Mirai           |  1923  |   21222   |   8 / 92   |
| CTU-Malware-Capture-42-1 | Trojan          |  4420  |     6     | 99.8 / 0.2 |
| CTU-Malware-Capture-44-1 | Mirai           |  211   |    26     |  90 / 10   |

**Attribute descriptions**

| Attribute         | Description                                                                 | Type     |
|:------------------|:----------------------------------------------------------------------------|:---------|
| `ts`              | Timestamp of the capture                                                    | `int`    |
| `uid`             | ID of the capture                                                           | `str`    |
| `id_orig.h`       | Originating IP where the attack happened                                    | `str`    |
| `id_orig.p`       | Port used by the responder                                                  | `int`    |
| `id_resp.h`       | IP address of the device on which capture happened.                         | `str`    |
| `id_resp.p`       | Port used from the response from the device on which the capture happened.  | `int`    |
| `proto`           | Network protocol                                                            | `str`    |
| `service`         | Application protocol                                                        | `str`    |
| `duration`        | Duration of the transmission between device and attacker.                   | `float`  |
| `orig_bytes`      | Amount of data sent to the device                                           | `int`    |
| `resp_bytes`      | Amount of data sent by the device                                           | `int`    |
| `conn_state`      | State of the connection                                                     | `str`    |
| `local_orig`      | the connection originated locally                                           | `bool`   |
| `local_resp`      | Whether the response originated locally                                     | `bool`   |
| `missed_bytes`    | Amount of missed bytes in a message                                         | `int`    |
| `history`         | History of the state of the connection                                      | `str`    |
| `orig_pkts`       | Amount of packets sent to the device                                        | `int`    |
| `orig_ip_bytes`   | Amount of bytes sent to the device                                          | `int`    |
| `resp_pkts`       | Amount of packets sent from the device                                      | `int`    |
| `resp_ip_bytes`   | Amount of bytes sent from the device                                        | `int`    |
| `tunnel_parents`  | ID of connection if tunneled                                                | `str`    |
| `label`           | Type of capture, benign or malicious                                        | `str`    |
| `detailed-label`  | Type of the malicious capture                                               | `str`    |

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

