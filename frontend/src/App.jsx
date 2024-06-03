import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { PageHome } from './pages/PageHome';
import { ListProduct } from './pages/ListProduct';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/home" />} />
        <Route path="/home" element={<PageHome />} />
        <Route path="list-product" element={<ListProduct />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App
