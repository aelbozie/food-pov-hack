import Box from "@mui/material/Box";

import AddByBarcode from "../components/AddByBarcode/AddByBarcode";
import ReusableButton from "../components/ReusableButton/ReusableButton";

const AddNewProduct = () => {
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
      <AddByBarcode />
      {/* <AddItemButton text="Scan" /> */}

      <ReusableButton text="Add Item Manually" backgroundColor="black" />
    </Box>
  );
};
export default AddNewProduct;
