<h1><u>IR Assignment </u></h1>  
- - -

<div>
  <h2>Problem Statement</h2>
  <p>
    Consider Boolean Retrieval with a set of 'n' documents
    <ul>
      <li> Let The query be any word that occurs in <b>n/2</b> documents.
      <li> Now using <b>star</b> operator for generating wild card queries.</li>
      <ol>
        <li><b>Star</b> can be a prefix Eg: 'foo<b>(star)</b>'.</li>
        <li><b>Star</b> can be a suffix Eg: '<b>(star)</b>ball'.</li>
        <li><b>star</b> can be any missing charachter/s between two given charachtersEg: H(<b>star</b>)O.</li>
      </ol>
    </ul>
    <i>NOTE: Take 10 documents with a minimum of 20 words each.</i>
  </p>
</div>

<div>
    <h2>Problem Solution</h2>
    <h3>Documents (Folder)</h3>
    <p>This folder contains the Corpus containing 10 documents (1.txt, 2.txt . . . 10.txt)<br> It contains Text about the Information Retrieval collected from different sources such as Wikipedia,AnalticsVidhya etc.</p>
    <h2>Main.py</h2>
    <p>
      This file contains the code to make the <b>inverted index</b> and <b>permuterm index</b> and stores them in <u>invertedIndex.txt</u> and <u>PermutermIndex.txt</u> respectively
    </p>
    <h3>Format to pass in Query</h3>
    <p>
      Similar to Weslaw system just add a '\' before every operation for Eg:<br>
      <h4>For Part 1<br></h4>
      <h5>Query</h5>
  
      `\NOT information \AND \NOT retrieval \or object`
      `information [1, 1, 1, 0, 0, 0, 0, 0, 0, 1]` <br>
      `retrieval [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]` <br>
      `object [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]` <br>
      `2.txt` <br>
      `3.txt` <br>
      `4.txt` <br>
      `5.txt` <br>
      `6.txt` <br>
      `8.txt` <br>
      `9.txt` <br>
      
        `\NOT inform*on \AND \NOT retri*l` 
        
      `4.txt` <br>
      `5.txt`<br>
      `6.txt`<br>
      `8.txt`<br>
      `9.txt`<br>
    </p>
</div>
