import Box from "@mui/material/Box";

import AddByBarcode from "../components/AddByBarcode/AddByBarcode";
import Button from "../components/Button/Button";

const AddNewProduct = () => {
  return (
    <Box
      p={3}
      height="70%"
      display="flex"
      flexDirection="column"
      justifyContent="space-around"
      //   sx={{ display: "flex", flexDirection: "column" }}
    >
      <AddByBarcode />
      {/* <AddItemButton text="Scan" /> */}
      {/* <Button text="Add Item Manually" backgroundColor="red" /> */}
      <Button text="Add Item Manually" backgroundColor="black" />
    </Box>
  );
};
export default AddNewProduct;
