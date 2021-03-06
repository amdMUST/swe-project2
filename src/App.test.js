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

test('Make sure article name is rendered', () => {
  render(<App />);
  const linkElement = screen.getByTestId("article_data1");
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
