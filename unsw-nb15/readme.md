# UNSW-NB15

**Description**

The raw network packets of the UNSW-NB 15 dataset was created by the IXIA PerfectStorm tool in the Cyber Range Lab of
UNSW Canberra for generating a hybrid of real modern normal activities and synthetic contemporary attack behaviours. The
tcpdump tool was utilised to capture 100 GB of the raw traffic (e.g., Pcap files). This dataset has nine types of
attacks, namely, Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode and Worms. The Argus,
Bro-IDS tools are used and twelve algorithms are developed to generate totally 49 features with the class label. These
features are described in UNSW-NB15_features.csv file.

- The total number of records is two million and 540,044 which are stored in the four CSV files, namely,
  UNSW-NB15_1.csv, UNSW-NB15_2.csv, UNSW-NB15_3.csv and UNSW-NB15_4.csv.
- The ground truth table is named UNSW-NB15_GT.csv and the list of event file is called UNSW-NB15_LIST_EVENTS.csv.
- A partition from this dataset was configured as a training set and testing set, namely, UNSW_NB15_training-set.csv and
  UNSW_NB15_testing-set.csv respectively. The number of records in the training set is 175,341 records and the testing
  set is 82,332 records from the different types, attack and normal.


**Data files & Format**

- Data converted to CSV format

**Attribute descriptions**

| No. | Name               | Type      | Description                                                                                                                           |
|:----|:-------------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------|
| 1   | `srcip`            | nominal   | Source IP address                                                                                                                     |
| 2   | `sport`            | integer   | Source port number                                                                                                                    |
| 3   | `dstip`            | nominal   | Destination IP address                                                                                                                |
| 4   | `dsport`           | integer   | Destination port number                                                                                                               |
| 5   | `proto`            | nominal   | Transaction protocol                                                                                                                  |
| 6   | `state`            | nominal   | Indicates to the state and its dependent protocol, e.g. ACC, CLO, CON, ...                                                            |
| 7   | `dur`              | Float     | Record total duration                                                                                                                 |
| 8   | `sbytes`           | Integer   | Source to destination transaction bytes                                                                                               |
| 9   | `dbytes`           | Integer   | Destination to source transaction bytes                                                                                               |
| 10  | `sttl`             | Integer   | Source to destination time to live value                                                                                              |
| 11  | `dttl`             | Integer   | Destination to source time to live value                                                                                              |
| 12  | `sloss`            | Integer   | Source packets retransmitted or dropped                                                                                               |
| 13  | `dloss`            | Integer   | Destination packets retransmitted or dropped                                                                                          |
| 14  | `service`          | nominal   | http, ftp, smtp, ssh, dns, ftp-data, irc  and (-) if not much used service                                                            |
| 15  | `Sload`            | Float     | Source bits per second                                                                                                                |
| 16  | `Dload`            | Float     | Destination bits per second                                                                                                           |
| 17  | `Spkts`            | integer   | Source to destination packet count                                                                                                    |
| 18  | `Dpkts`            | integer   | Destination to source packet count                                                                                                    |
| 19  | `swin`             | integer   | Source TCP window advertisement value                                                                                                 |
| 20  | `dwin`             | integer   | Destination TCP window advertisement value                                                                                            |
| 21  | `stcpb`            | integer   | Source TCP base sequence number                                                                                                       |
| 22  | `dtcpb`            | integer   | Destination TCP base sequence number                                                                                                  |
| 23  | `smeansz`          | integer   | Mean of the ?ow packet size transmitted by the src                                                                                    |
| 24  | `dmeansz`          | integer   | Mean of the ?ow packet size transmitted by the dst                                                                                    |
| 25  | `trans_depth`      | integer   | Represents the pipelined depth into the connection of http request/response transaction                                               |
| 26  | `res_bdy_len`      | integer   | Actual uncompressed content size of the data transferred from the server's http service.                                              |
| 27  | `Sjit`             | Float     | Source jitter (mSec)                                                                                                                  |
| 28  | `Djit`             | Float     | Destination jitter (mSec)                                                                                                             |
| 29  | `Stime`            | Timestamp | record start time                                                                                                                     |
| 30  | `Ltime`            | Timestamp | record last time                                                                                                                      |
| 31  | `Sintpkt`          | Float     | Source interpacket arrival time (mSec)                                                                                                |
| 32  | `Dintpkt`          | Float     | Destination interpacket arrival time (mSec)                                                                                           |
| 33  | `tcprtt`           | Float     | TCP connection setup round-trip time, the sum of synack and ackdat.                                                                   |
| 34  | `synack`           | Float     | TCP connection setup time, the time between the SYN and the SYN_ACK packets.                                                          |
| 35  | `ackdat`           | Float     | TCP connection setup time, the time between the SYN_ACK and the ACK packets.                                                          |
| 36  | `is_sm_ips_ports`  | Binary    | If source (1) and destination (3) IP addresses equal and port numbers (2)(4) equal then, this variable takes value 1 else 0           |
| 37  | `ct_state_ttl`     | Integer   | No. for each state (6) according to specific range of values for source/destination time to live (10) (11).                           |
| 38  | `ct_flw_http_mthd` | Integer   | No. of flows that has methods such as Get and Post in http service.                                                                   |
| 39  | `is_ftp_login`     | Binary    | If the ftp session is accessed by user and password then 1 else 0.                                                                    |
| 40  | `ct_ftp_cmd`       | integer   | No of flows that has a command in ftp session.                                                                                        |
| 41  | `ct_srv_src`       | integer   | No. of connections that contain the same service (14) and source address (1) in 100 connections according to the last time (26).      |
| 42  | `ct_srv_dst`       | integer   | No. of connections that contain the same service (14) and destination address (3) in 100 connections according to the last time (26). |
| 43  | `ct_dst_ltm`       | integer   | No. of connections of the same destination address (3) in 100 connections according to the last time (26).                            |
| 44  | `ct_src_ ltm`      | integer   | No. of connections of the same source address (1) in 100 connections according to the last time (26).                                 |
| 45  | `ct_src_dport_ltm` | integer   | No of connections of the same source address (1) and the destination port (4) in 100 connections according to the last time (26).     |
| 46  | `ct_dst_sport_ltm` | integer   | No of connections of the same destination address (3) and the source port (2) in 100 connections according to the last time (26).     |
| 47  | `ct_dst_src_ltm`   | integer   | No of connections of the same source (1) and the destination (3) address in in 100 connections according to the last time (26).       |
| 48  | `attack_cat`       | nominal   | The name of each attack category. In this data set, nine categories                                                                   |
| 49  | `Label`            | binary    | 0 for normal and 1 for attack records                                                                                                 |

**Dataset source**

<https://research.unsw.edu.au/projects/unsw-nb15-dataset/>

(see: _"The UNSW-NB15 source files ... can be downloaded from HERE."_)

**Reuse & Papers**

There are some papers published by the authors for developing, Intrusion Detection, Network Forensics, and
Privacy-preserving, and Threat Intelligence approaches in different systems, such as Network Systems, Internet of
Things (IoT), SCADA, Industrial IoT, and Industry 4.0. It is preferable to cite the following papers while comparing
with your studies:

- Moustafa, Nour, et al. "An Ensemble Intrusion Detection Technique based on proposed Statistical Flow Features for
  Protecting Network Traffic of Internet of Things." IEEE Internet of Things Journal (2018).
- Koroniotis, Nickolaos, Moustafa, Nour, et al. "Towards Developing Network Forensic Mechanism for Botnet Activities in
  the IoT Based on Machine Learning Techniques." International Conference on Mobile Networks and Management. Springer,
  Cham, 2017.
- Moustafa, Nour, et al. "Generalized Outlier Gaussian Mixture technique based on Automated Association Features for
  Simulating and Detecting Web Application Attacks." IEEE Transactions on Sustainable Computing (2018).
- Keshk, Marwa, Moustafa, Nour, et al. "Privacy preservation intrusion detection technique for SCADA systems." Military
  Communications and Information Systems Conference (MilCIS), 2017. IEEE, 2017.
- Moustafa, Nour, et al. "A New Threat Intelligence Scheme for Safeguarding Industry 4.0 Systems." IEEE Access (2018).
- Moustafa, Nour, et al. "Anomaly Detection System Using Beta Mixture Models and Outlier Detection." Progress in
  Computing, Analytics and Networking. Springer, Singapore, 2018. 125-135.
- Moustafa, Nour, et al. "Flow Aggregator Module for Analysing Network Traffic." Progress in Computing, Analytics and
  Networking. Springer, Singapore, 2018. 19-29.
- Moustafa, Nour, et al. "A Network Forensic Scheme Using Correntropy-Variation for Attack Detection." IFIP
  International Conference on Digital Forensics. Springer, Cham, 2018.

For more information about designing the new algorithms of the features published in the UNSW-NB15 dataset, please cite
Dr.Nour Moustafa’s thesis. The details of the algorithms have been published in Chapter 3.

Moustafa, Nour. Designing an online and reliable statistical anomaly detection framework for dealing with large
high-speed network traffic. Diss. University of New South Wales, Canberra, Australia, 2017.

Free use of the UNSW-NB15 dataset for academic research purposes is hereby granted in perpetuity. Use for commercial
purposes should be agreed by the authors. Nour Moustafa and Jill Slay have asserted their rights under the Copyright. To
whom intend the use of the UNSW-NB15 dataset have to cite the above five papers.

For more information about the datasets, please contact the author, Dr Nour Moustafa, on his email:
nour.moustafa@unsw.edu.au or nour.moustafa@ieee.org.
