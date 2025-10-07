from mars_probe_api.probes.models import Probe
from mars_probe_api.probes.payloads import CommandEnum, DirectionEnum
from mars_probe_api.store.mysqlstore import SQLAlchemySession


class ProbeService:
    @classmethod
    def create_probe(
        cls,
        terrain_length: int,
        terrain_width: int,
        direction: DirectionEnum,
        db_session: SQLAlchemySession,
    ) -> Probe:
        probe = Probe(
            direction=direction.value,
            terrain_length=terrain_length,
            terrain_width=terrain_width,
        )
        db_session.add(probe)
        db_session.flush()

        return probe

    @classmethod
    def get_all_probes(
        cls,
        db_session: SQLAlchemySession,
    ) -> list[Probe]:
        return db_session.query(Probe).order_by(Probe.id).all()

    @classmethod
    def get_probe_by_id(
        cls,
        id: str,
        db_session: SQLAlchemySession,
    ) -> Probe:
        return db_session.query(Probe).filter(Probe.id == id).one_or_none()

    @classmethod
    def move_probe(
        cls,
        probe: Probe,
        commands: str,
        db_session: SQLAlchemySession,
    ) -> Probe:
        """
        Move a sonda em um terreno com base em uma sequência de comandos.
        Este método atualiza a posição e direção de uma sonda no terreno,
        seguindo os comandos fornecidos. Ele também valida os movimentos
        para garantir que a sonda não ultrapasse os limites do terreno.
        Args:
            probe (Probe): A sonda que será movida.
            commands (str): Uma sequência de comandos a serem executados.
                Os comandos podem incluir:
                    - "M" (MOVE_FORWARD): Move a sonda para frente na direção atual.
                    - "R" (TURN_RIGHT): Gira a sonda 90 graus para a direita.
                    - "L" (TURN_LEFT): Gira a sonda 90 graus para a esquerda.
            db_session (SQLAlchemySession): Sessão do banco de dados para persistir as alterações.
        Returns:
            Probe: A sonda atualizada com a nova posição e direção.
        Raises:
            ValueError: Se um movimento inválido for detectado, como ultrapassar
            os limites do terreno.
        """

        current_direction = probe.direction
        current_pos_x = probe.x
        current_pos_y = probe.y
        directions_ordered = [direction.value for direction in DirectionEnum]
        direction_index = directions_ordered.index(current_direction)

        for command in commands:
            if command == CommandEnum.MOVE_FORWARD.value:
                match (current_direction):
                    case DirectionEnum.NORTH.value:
                        current_pos_y += 1
                    case DirectionEnum.SOUTH.value:
                        current_pos_y -= 1
                    case DirectionEnum.EAST.value:
                        current_pos_x += 1
                    case DirectionEnum.WEST.value:
                        current_pos_x -= 1

                if (
                    current_pos_x < 0
                    or current_pos_y < 0
                    or current_pos_x > probe.terrain_width
                    or current_pos_y > probe.terrain_width
                ):
                    raise ValueError("Invalid movement")

            if command == CommandEnum.TURN_RIGHT.value:
                direction_index = (direction_index + 1) % len(
                    directions_ordered
                )  # Caso tenha uma volta horária completa retorna ao começo
                current_direction = directions_ordered[direction_index]

            if command == CommandEnum.TURN_LEFT.value:
                direction_index = (direction_index - 1) % len(
                    directions_ordered
                )  # Caso tenha uma volta anti-horária completa retorna ao começo
                current_direction = directions_ordered[direction_index]

        probe.x = current_pos_x
        probe.y = current_pos_y
        probe.direction = current_direction
        db_session.flush()

        return probe
