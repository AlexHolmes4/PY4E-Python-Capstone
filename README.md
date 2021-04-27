"# Python-Repository" 

<h1>PY4E - CAPSTONE PROJECT</h1>

<h3>Overview</h3>
For the final (optional) assignment of the PY4E specalization students were to pick a data source, analyse it and visually represent patterns. I chose <a href = https://academictorrents.com/details/a2ccf94bbb4af222bf8e69dad60a68a29f310d9a> flight data from academic torrents </a>. 

<h4>High Level Solution Architecture</h4>
![flightdatacrawler High Level Overview](https://user-images.githubusercontent.com/55677663/116175843-abafba80-a743-11eb-9075-259e9b974545.PNG)
<ul>
  <li> A python program will run and extract the data into a raw storage database. This first extraction of data is unstructured, the stopping and restarting of data extraction will be incorperated in the python program - SQL query design. </li>
  <li> The data can be processed, modelled and stored into a second structured relational database where querying is optimized. </li>
  <li>This data can now visualized using Javascript. The D3 (Data Driven Documents) Javascript Library was chosen for the visualisation. </li>
 </ul>
 <u>Solution Architecture - Multi Layered Analysis</u>
![flightdatacrawler High Level Solution](https://user-images.githubusercontent.com/55677663/116177451-604adb80-a746-11eb-9e15-af3482967d9d.PNG)
