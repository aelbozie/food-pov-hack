import Box from "@mui/material/Box";
import { useState } from "react";

import IconButton from "@mui/material/IconButton";
import NavigateBeforeIcon from "@mui/icons-material/NavigateBefore";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";

import logo1 from "../../assets/logo1.PNG";

const Header = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  return (
    <Container maxWidth="xl">
      <Box
        pt={2}
        sx={{
          justifySelf: "flex-start",

          display: "flex",
          justifyContent: "space-between",
        }}
      >
        <IconButton sx={{ p: 0 }}>
          <NavigateBeforeIcon sx={{ color: "black" }} />
        </IconButton>
        <img src={logo1} width="85px" alt="logo" m={5} />

        {isLoggedIn ? (
          <IconButton sx={{ p: 0 }}>
            <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
          </IconButton>
        ) : (
          <p style={{ width: "20px" }}></p>
        )}
      </Box>
    </Container>
  );
};
export default Header;
