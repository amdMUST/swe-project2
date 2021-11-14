import { render, screen } from '@testing-library/react';
import App from './App';

test('Make sure city name is rendered', () => {
  render(<App />);
  const linkElement = screen.getByTestId("CityTitle");
  expect(linkElement).toBeInTheDocument();
});


test('Make sure location in city is rendered', () => {
  render(<App />);
  const linkElement = screen.getByTestId("CityLocation");
  expect(linkElement).toBeInTheDocument();
});

test('Make sure images of cities are rendered', () => {
  render(<App />);
  const linkElement = screen.getByTestId("CityImages");
  expect(linkElement).toBeInTheDocument();
});
