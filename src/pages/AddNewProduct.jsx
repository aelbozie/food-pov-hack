import Box from "@mui/material/Box";
import React, { useEffect, useState } from "react";
import AddByBarcode from "../components/AddByBarcode/AddByBarcode";
import ReusableButton from "../components/ReusableButton/ReusableButton";
import AddManual from "../components/AddManual/AddManual";
const AddNewProduct = () => {
  const [data, setData] = useState("");

  const [scan, setScan] = useState(false);
  const [product, setProduct] = useState([]);
  const URL = `https://world.openfoodfacts.org/api/v0/product/${data}.json`;
  useEffect(() => {
    try {
      const fetchData = async () => {
        const response = await fetch(
          `https://world.openfoodfacts.org/api/v0/product/${data}.json`
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
  //
  return (
    <Box
      p={3}
      height="70%"
      display="flex"
      flexDirection="column"
      justifyContent="space-around"
      alignItems="center"
      //   sx={{ display: "flex", flexDirection: "column" }}
    >
      {/* <AddItemButton text="Scan" /> */}
      {!data ? (
        <AddByBarcode
          scan={scan}
          setData={setData}
          setScan={setScan}
          data={data}
          product={product}
        />
      ) : (
        <AddManual product={product} />
      )}
      {/* <ReusableButton text="Add Item Manually" backgroundColor="black" /> */}
    </Box>
  );
};
export default AddNewProduct;
