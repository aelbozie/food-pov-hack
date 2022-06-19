import Container from "@mui/material/Container";
import Box from "@mui/material/Box";
import "./App.css";
import Header from "./components/Header/Header";
import NavBar from "./components/NavBar/NavBar";
import AddNewProduct from "./pages/AddNewProduct";
import AddManual from "./components/AddManual/AddManual";

function App() {
  return (
    <Container
      sx={{
        maxWidth: "390px",
        minHeight: "844px",
        padding: "0",
        height: "100%",
        borderCollapse: "collapse",
        display: "flex",
        flexDirection: "column",

        overflowY: "hidden",
      }}
    >
      <Header />
      <Box
        sx={{
          overflowY: "scroll",
          height: "calc(100vh - 129.55px)",
        }}
      >
        <AddNewProduct />
        {/* <AddManual /> */}
        {/* <AddNewProduct />
        <AddNewProduct /> */}
      </Box>
      <NavBar />
    </Container>
  );
}

export default App;
