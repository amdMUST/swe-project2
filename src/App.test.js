import { render, screen } from '@testing-library/react';
import App from './App';

test('Make sure city name is rendered', () => {
  render(<App />);
  const linkElement = screen.getByTestId("CityTitle");
  expect(linkElement).toBeInTheDocument();
});
