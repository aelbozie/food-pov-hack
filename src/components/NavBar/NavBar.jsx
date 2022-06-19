import Box from "@mui/material/Box";
import { useState } from "react";
import BottomNavigation from "@mui/material/BottomNavigation";
import BottomNavigationAction from "@mui/material/BottomNavigationAction";
import HomeIcon from "@mui/icons-material/Home";
import AddIcon from "@mui/icons-material/Add";
import FormatListBulletedIcon from "@mui/icons-material/FormatListBulleted";

const NavBar = () => {
  const [value, setValue] = useState(0);
  return (
    <Box sx={{ maxWidth: "sm" }}>
      <BottomNavigation
        showLabels
        value={value}
        onChange={(event, newValue) => {
          setValue(newValue);
        }}
      >
        <BottomNavigationAction
          label="Home"
          sx={{ color: "black" }}
          icon={<HomeIcon />}
        />
        <BottomNavigationAction
          label="Add"
          icon={<AddIcon />}
          sx={{ color: "black" }}
        />
        <BottomNavigationAction
          label="All Items"
          sx={{ color: "black" }}
          icon={<FormatListBulletedIcon />}
        />
      </BottomNavigation>
    </Box>
  );
};
export default NavBar;
