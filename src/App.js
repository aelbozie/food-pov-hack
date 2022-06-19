import Container from "@mui/material/Container";
import "./App.css";
import Header from "./components/Header/Header";
import NavBar from "./components/NavBar/NavBar";
import AddNewProduct from "./pages/AddNewProduct";

function App() {
  return (
    <Container
      sx={{
        padding: "0",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
      }}
    >
      <Header />
      <AddNewProduct />
      <NavBar />
    </Container>
  );
}

export default App;
