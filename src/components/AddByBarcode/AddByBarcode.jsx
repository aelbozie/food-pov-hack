import React, { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import BarcodeScannerComponent from "react-qr-barcode-scanner";
import AddManual from "../AddManual/AddManual";
const AddByBarcode = () => {
  const [data, setData] = useState("Not Found");

  const [scan, setScan] = useState(false);
  const [product, setProduct] = useState([]);
  const URL = `https://world.openfoodfacts.org/api/v0/product/${5053990138722}.json`;

  useEffect(() => {
    try {
      const fetchData = async () => {
        const response = await fetch(
          `https://world.openfoodfacts.org/api/v0/product/${5053990138722}.json`
        );
        const product = await response.json();
        //id,product_name,compared_to_category,_keywords
        setProduct(product.product);
        console.log(product.product);
      };

      data && fetchData();
    } catch (error) {
      console.log(error.message);
    }
  }, [URL, data]);

  return (
    <Box>
      {scan && (
        <BarcodeScannerComponent
          width={400}
          height={200}
          onUpdate={(err, result) => {
            if (result) {
              setData(result.text);
              setScan(false);
              console.log(data);
            } else setData("Not Found");
          }}
        />
      )}
      <button onClick={() => setScan(true)}>SCAN</button>
      <button onClick={() => setScan(false)}>CANCEL</button>
      <p>{data}</p>
      {product && <AddManual product={product.product_name} />}
    </Box>
  );
};
export default AddByBarcode;
