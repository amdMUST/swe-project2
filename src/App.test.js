import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/City Name/i);
  const textInput = screen.getByTestId('s132');
  expect(linkElement).toBeInTheDocument();
});
