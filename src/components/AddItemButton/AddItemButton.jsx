import Button from "@mui/material/Button";

const AddItemButton = () => {
  return (
    <Button
      variant="contained"
      size="large"
      sx={{
        backgroundColor: "black",
        textTransform: "none",
        margin: "50px",
        borderRadius: "7px",
        fontWeight: "normal",
      }}
    >
      Add item manually
    </Button>
  );
};
export default AddItemButton;
