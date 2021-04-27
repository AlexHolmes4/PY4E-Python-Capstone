

<h1>PY4E - CAPSTONE PROJECT</h2>

<h2>Overview</h2>
For the final (optional) assignment of the PY4E specalization students were to pick a data source, analyse it and visually represent patterns. I chose <a href = https://academictorrents.com/details/a2ccf94bbb4af222bf8e69dad60a68a29f310d9a> flight data from academic torrents </a>. This data was too large to upload to the repository reliably, but you can download from the source link above as a tsv file. 


<h3>"High Level Solution Architecture"</h3>

![flightdatacrawler High Level Overview](https://user-images.githubusercontent.com/55677663/116178867-d9e3c900-a748-11eb-8f0f-f5dbab3d3708.PNG) 

<ul>
  <li> A python program will run and extract the data into a raw storage database. This first extraction of data is unstructured, the stopping and restarting of data extraction will be incorperated in the python program - SQL query design. </li>
  <li> The data can be processed, modelled and stored into a second structured relational database where querying is optimized. </li>
  <li>This data can now visualized using Javascript. The D3 (Data Driven Documents) Javascript Library was chosen for the visualisation. </li>
 </ul>
 
 <h3>Solution Architecture - Multi Layered Analysis</h3>

![flightdatacrawler High Level Solution](https://user-images.githubusercontent.com/55677663/116178864-d81a0580-a748-11eb-8cce-ed0ca93e058b.PNG)

<h3>Data Model</h3>

![data model flights](https://user-images.githubusercontent.com/55677663/116188803-93976580-a75a-11eb-9730-d054eab357a9.PNG)
