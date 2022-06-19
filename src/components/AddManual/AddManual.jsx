import Box from "@mui/material/Box";
import IconButton from "@mui/material/IconButton";
import RemoveIcon from "@mui/icons-material/Remove";

import AddIcon from "@mui/icons-material/Add";
import FormControl from "@mui/material/FormControl";
import TextField from "@mui/material/TextField";

import ReusableButton from "../ReusableButton/ReusableButton";

import MenuItem from "@mui/material/MenuItem";
import Typography from "@mui/material/Typography";

import Select from "@mui/material/Select";
import { Input } from "@mui/material";
const categories = [
  "Food cupboard",
  "Toiletries",
  "Household",
  "Baby",
  "Miscellaneous",
];
const AddManual = () => {
  return (
    <Box
      component="form"
      display="flex"
      flexDirection="column"
      justifyContent="space-between"
      p={3}
      fullWidth
      noValidate
      height="80%"
      autoComplete="off"
    >
      <FormControl>
        <Typography mb={2}>Item name</Typography>
        <TextField
          fullWidth
          required
          id="outlined-required"
          label="Item name"
        />
      </FormControl>

      <FormControl>
        <Typography mb={2}>Item category</Typography>
        <Select fullWidth label="Item Category" required>
          {categories.map((category, index) => (
            <MenuItem key={index} value={category}>
              {category}
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
          <IconButton
            size="small"
            sx={{
              borderRadius: "100%",
              backgroundColor: "black",
              color: "white",
            }}
          >
            <RemoveIcon />
          </IconButton>
          <Input
            sx={{
              width: "20%",
              textAlign: "center",
              border: "none",
              outline: "none",
            }}
          />
          <IconButton
            size="small"
            sx={{
              borderRadius: "100%",
              backgroundColor: "green",
              color: "white",
            }}
          >
            <AddIcon />
          </IconButton>
        </Box>
      </Box>
      <ReusableButton text="Add" backgroundColor="black" />
    </Box>
  );
};
export default AddManual;
