import Button from "@mui/material/Button";

const AddItemButton = (props) => {
  return (
    <Button
      variant="contained"
      size={props.size}
      sx={{
        backgroundColor: props.backgroundColor,
        textTransform: "none",
        margin: "50px",
        borderRadius: "7px",
        fontWeight: "normal",
      }}
      type={props.type}
    >
      {props.text}
    </Button>
  );
};
export default AddItemButton;
