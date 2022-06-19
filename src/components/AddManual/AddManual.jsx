import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import RemoveIcon from "@mui/icons-material/Remove";
import Button from "@mui/material/Button";
import AddIcon from "@mui/icons-material/Add";
import FormControl from "@mui/material/FormControl";
import TextField from "@mui/material/TextField";

import ReusableButton from "../ReusableButton/ReusableButton";

import MenuItem from "@mui/material/MenuItem";
import Typography from "@mui/material/Typography";

import Select from "@mui/material/Select";
import { Input } from "@mui/material";
import { useState } from "react";
const categories = [
  "Food cupboard",
  "Toiletries",
  "Household",
  "Baby",
  "Miscellaneous",
];
const AddManual = ({ product }) => {
  const [itemName, setItemName] = useState(product);
  const [category, setCategory] = useState("");
  const [quantity, setQuantity] = useState(1);

  const handleCategoryChange = (e) => {
    setCategory(e.target.value);
    console.log(category);
  };
  const incrementQuantity = () => setQuantity(quantity + 1);
  const decrementQuantity = () => setQuantity(quantity - 1);
  if (quantity <= 0) {
    setQuantity(1);
  }
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(product, category, quantity);
  };
  return (
    <Box
      component="form"
      display="flex"
      flexDirection="column"
      justifyContent="space-between"
      p={3}
      fullWidth
      noValidate
      height="100%"
      autoComplete="off"
      onSubmit={handleSubmit}
    >
      <FormControl>
        <Typography mb={2}>Item name</Typography>

        <TextField fullWidth required id="outlined-required" value={product} />
      </FormControl>
      {itemName}
      <FormControl>
        <Typography mb={2}>Item category</Typography>
        <Select
          fullWidth
          label="Item Category"
          required
          value={category}
          onChange={handleCategoryChange}
        >
          {categories.map((x, index) => (
            <MenuItem key={index} value={x}>
              {x}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
      <Box
        fullWidth
        sx={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <Typography>Quantity</Typography>

        <Box width="40%" display="flex" justifyContent="space-between">
          <Button
            sx={{
              minWidth: "30px",
              height: "30px",

              padding: "0px",
              borderRadius: "50%",
              "&:hover": {
                backgroundColor: "black",
                borderColor: "#0062cc",
                boxShadow: "none",
              },
              backgroundColor: "black",
              color: "white",
            }}
            onClick={decrementQuantity}
          >
            -
          </Button>
          <Input
            sx={{
              width: "20%",
              textAlign: "center",
              border: "none",
              outline: "none",
            }}
            value={quantity}
          />
          <Button
            sx={{
              minWidth: "30px",
              height: "30px",
              "&:hover": {
                backgroundColor: "green",
                borderColor: "#0062cc",
                boxShadow: "none",
              },
              padding: "0px",
              borderRadius: "50%",
              backgroundColor: "green",
              color: "white",
            }}
            onClick={incrementQuantity}
          >
            +
          </Button>
        </Box>
      </Box>
      <ReusableButton text="Add" backgroundColor="black" type="submit" />
    </Box>
  );
};
export default AddManual;
