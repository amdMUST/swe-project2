import { render, screen } from '@testing-library/react';
import App from './App';

test('Make sure city name is rendered', () => {
  render(<App />);
  const cityTitle = screen.getByTestId("CityTitle");
  expect(cityTitle).toBeInTheDocument();
});

test('Make sure we have the users google info', () => {
  render(<App />);
  const userinfo = screen.getByTestId("user-info");
  expect(userinfo).toBeInTheDocument();
});
