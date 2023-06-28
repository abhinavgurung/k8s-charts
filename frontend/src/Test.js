import React, { useEffect, useState } from "react";
import axios from "axios";

function Test() {
  const [result, setResult] = useState({});

//   useEffect(() => {
//     axios.get("http://localhost:5000/test").then((response) => {
//       console.log(response.data);
//       setResult(()=>);
//     });
//   }, []);

  async function  callApi() {
      let res = null;

      res = await axios("http://localhost:5000/test");
      console.log(res.data);
      setResult(res.data);

  };

  return (
    <div>
      <h3>Data From Test api from backend</h3>
      <button onClick={callApi}>Call Test api</button>
      <p>{result.level}</p>
      <p>{result.department}</p>
      <p>{result.school}</p>
    </div>
  );
}

export default Test;