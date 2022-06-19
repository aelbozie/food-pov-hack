import Box from "@mui/material/Box";

import AddByBarcode from "../components/AddByBarcode/AddByBarcode";
import AddItemButton from "../components/AddItemButton/AddItemButton";

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
      <AddItemButton />
    </Box>
  );
};
export default AddNewProduct;
